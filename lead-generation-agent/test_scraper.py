from src.graph.nodes.scrape_node import scrape_node

# Mock State
initial_state = {
    "leads": [
        {
            "company_name": "Example Domain",
            "url": "https://example.com",
            "description": "",
            "status": "new"
        }
    ]
}

print("🕷️ Running Scraper Test...")
try:
    result = scrape_node(initial_state)
    
    leads = result["leads"]
    for lead in leads:
        print(f"\n✅ Scraped: {lead['company_name']}")
        print(f"📄 Status: {lead['status']}")
        print(f"📝 Content Preview: {lead['description'][:100]}...") # Show first 100 chars

except Exception as e:
    print(f"\n❌ Test Failed: {e}")
    import traceback
    traceback.print_exc()
