import re 
from src.graph.state import LeadState

def email_node(state: LeadState) -> dict:
    """
    Extracts email from the text or guess one based in the domain 

    """

    leads = state.get("leads")

    leads_to_process = [lead for lead in leads if lead.get("status") == "qualified" ]
    if not leads_to_process:
        print("No qualified leads to process for email extraction.")
        return {"leads": leads}
    
    for lead in leads_to_process:
        print(f"Processing lead for email extraction: {lead.get('company_name')}")

        text = lead.get("description","")
        url = lead.get("url","")

        email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
        emails_found = re.findall(email_pattern, text)

        valid_emails = [e for e in emails_found if not e.endswith(('.png', '.jpg', '.jpeg', '.gif', 'example.com'))]

        if valid_emails:
            lead['email'] = valid_emails[0]
            print(f" -> Extracted email from text: {lead['email']}")
        else:
            try:
                from urllib.parse import urlparse
                parsed_url = urlparse(url)
                domain = parsed_url.netloc.replace('www.', '')
                if domain:
                    guessed_email = f"info@{domain}"
                    lead['email'] = guessed_email
                else:
                    lead['email'] = "Not found"
            except Exception as e:
                print(f"Error guessing email for {lead.get('company_name')}: {e}")
                lead['email'] = "Not found"

    return {"leads": leads}