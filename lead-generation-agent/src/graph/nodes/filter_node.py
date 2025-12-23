import os
import json
from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from src.graph.state import LeadState

def filter_node(state: LeadState) -> dict:
    """
    Use LLm to filter leads based ont he ICP crieteria
    """
    leads = state.get("leads")

    leads_to_scrape = [lead for lead in leads if lead.get("status") == "scraped"]

    if not leads_to_scrape:
        print("No new scraped leads to extract from.")
        return {"leads": leads}

    extracted_leads = []
    
    # Initialize LLM with a smaller model to save tokens and avoid rate limits
    llm = ChatGroq(model="llama-3.1-8b-instant", temperature=0, api_key=os.getenv("GROQ_API_KEY"))
    
    # Extraction Prompt
    prompt = PromptTemplate.from_template(
        """You are a Lead Generation Specialist.
        
        Analyze the following text from a search result and extract details of companies that match the criteria.
        
        Text Content:
        {description}
        
        Criteria: The company must be related to "AI", "Technology", "Machinery", or "Marketing" (and specifically {query} if relevant).
        
        Task:
        1. Identify any companies mentioned in the text that fit the criteria.
        2. For each company, extract:
           - Name
           - Summary (What they do)
           - Score (0-100 relevance)
           - Status ("qualified" if score > 70 else "disqualified")
           - Pitch (A generic one-liner opening for a cold email)
        
        Return ONLY a JSON list of objects. Format:
        [
            {{
                "company_name": "Example AI",
                "summary": "Building AGI for healthcare.",
                "score": 95,
                "status": "qualified",
                "pitch": "I saw Example AI is revolutionizing healthcare..."
            }}
        ]
        
        If no companies are found, return [].
        """)
    
    for lead in leads_to_scrape:
        print(f"Extracting companies from article: {lead.get('company_name')}")
        try:
            chain = prompt | llm
            
            # Truncate text to 2500 chars (~600 tokens) to save usage
            full_text = lead.get("description", "")
            truncated_text = full_text[:2500] if full_text else ""

            response = chain.invoke({
                "description": truncated_text,
                "query": "target industry" 
            })

            content = response.content.strip()

            if "```json" in content:
                content = content.split("```json")[1].split("```")[0].strip()
            elif "```" in content:
                content = content.split("```")[1].strip()
            
            # Parse list of companies
            companies = json.loads(content)
            
            if isinstance(companies, list):
                for company in companies:
                    if company.get("status") == "qualified":
                        new_lead = {
                            "company_name": company.get("company_name"),
                            "url": lead.get("url"), # Keep source URL
                            "description": lead.get("description"), # Keep full text? Or just summary? Maybe summary is better.
                            "summary": company.get("summary"),
                            "score": company.get("score"),
                            "email": "",
                            "pitch": company.get("pitch"),
                            "status": "qualified"
                        }
                        extracted_leads.append(new_lead)
                        print(f" -> Found: {new_lead['company_name']}")
            else:
                 print("LLM did not return a list.")

        except Exception as e:
            print(f"Error during extraction: {e}")
            # If extraction fails, maybe keep the original lead but mark as manual review? 
            # For now, we skip.
        
    return {"leads": extracted_leads[:5]}


