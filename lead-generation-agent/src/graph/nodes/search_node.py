from ddgs import DDGS
from src.graph.state import LeadState

def search_node(state:LeadState) -> dict:
    """
    Search for the companines using the duckduckgo search API and return the results.
    """

    query = state.get("search_query")
    max_results = state.get("max_results")
    
    # Construct query if not provided directly
    if not query:
        industry = state.get("industry", "")
        territory = state.get("territory", "")
        tech_stack = state.get("tech_stack", "")
        
        query = f"{industry} companies in {territory}"
        if tech_stack:
            query += f" using {tech_stack}"
    
    print(f"Searching for companies with query: {query} and max results: {max_results}")

    try:
        results = DDGS().text(query, max_results=max_results, region="in-en")

        print(f"DEBUG RAW RESULTS: {results}")
        new_leads = []
        if results:
            for result in results:
                lead = {
                    "company_name": result.get("title", "Unknown"),
                    "url": result.get("href", " "),
                    "description": result.get("body", " "),
                    "score": 0,
                    "email": "",
                    "summary": "",
                    "pitch": "",
                    "status": "new"
                }
                new_leads.append(lead)
                print(f"Found number of leads: {len(new_leads)} ")
        return {"leads": new_leads}
    except Exception as e:
        print(f"Error during search: {e}")
        new_leads = []
        return {"leads": new_leads}