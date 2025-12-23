from src.graph.nodes.email_node import email_node

# Mock State with qualified leads
initial_state = {
    "leads": [
        {
            "company_name": "Email Inc",
            "url": "https://email-inc.com",
            # This one has an email in text
            "description": "Contact us at support@email-inc.com for more info.",
            "status": "qualified"
        },
        {
            "company_name": "No Email Corp",
            "url": "https://no-email.io",
            # This one has NO email -> Should trigger guess
            "description": "We are a stealth startup.",
            "status": "qualified"
        }
    ]
}

print("📧 Running Email Hunter Test...")
try:
    result = email_node(initial_state)
    
    leads = result["leads"]
    for lead in leads:
        print(f"\n🏢 {lead['company_name']}")
        print(f"   URL: {lead['url']}")
        print(f"   Email Found: {lead.get('email', 'None')}")

except Exception as e:
    print(f"\n❌ Test Failed: {e}")
    import traceback
    traceback.print_exc()
