import os 

from langchain_groq import ChatGroq
from langchain_core.prompts import PromptTemplate
from src.graph.state import LeadState

def write_node(state: LeadState) -> dict:
    """
    Genrates cold emial pitches for the qualified leads
    """

    leads = state.get("leads")
    leads_to_pitch = [lead for lead in leads if lead.get("status") == "qualified"]

    if not leads_to_pitch:
        print("No qualified leads to pitch.")
        return {"leads": leads}

    llm  = ChatGroq(model="llama-3.3-70b-versatile", temperature=0, api_key = os.getenv("GROQ_API_KEY"))
    prompt = PromptTemplate.from_template(
        """
        You are a top tier B2B sale copywriter. Write cold emial for this prospect.

        Prospect company: {company_name}
        Description: {description}
        Summary: {summary}

        Our offer: A "Lead Genration Ai agent" that automates the process of finding and reaching out to potential clients using AI technology.
        Requiredments:
        1. Subject line catchy, under 6 words.
        2. Body: Under 100 words. Mention a specific detail from their description to prove we researched them.
        3. Tone: Professionla but converstional.
        4. Call to action: Ask for a qucil 15-min demo.

        Return ONLY the meial content (subject+body)
        """
    )
    for lead in leads_to_pitch:
        print(f"\n Pitching: {lead['company_name']}")
        try:
            chain = prompt | llm
            response = chain.invoke({
                "company_name": lead.get("company_name"),
                "description": lead.get("description"),
                "summary": lead.get("summary")
            })

            lead['pitch'] = response.content.strip()
            lead['status'] = 'pitched'
            print(f"\n Pitched: {lead['company_name']}\n{lead['pitch']}")
        except Exception as e:
            print(f"Error during pitching: {e}")
            lead['status'] = 'manual_review'
    
    return {"leads": leads}



        