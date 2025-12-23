from src.graph.nodes.filter_node import filter_node
from dotenv import load_dotenv

load_dotenv()

# Mock State with a 'scraped' lead
initial_state = {
    "leads": [
        {
            "company_name": "TechFlow AI",
            "url": "https://techflow.ai",
            "description": "TechFlow AI provides advanced artificial intelligence solutions for marketing automation. Our platform helps businesses scale their outreach using machine learning.",
            "status": "scraped",
            "score": 0,
            "summary": "",
            "pitch": ""
        },
        {
            "company_name": "Bob's Burgers",
            "url": "https://bobsburgers.com",
            "description": "Family owned burger joint serving the best burgers in town. best fries and shakes.",
            "status": "scraped",
            "score": 0,
            "summary": "",
            "pitch": ""
        }
    ]
}

print("🧠 Running ICP Filter Test...")
try:
    result = filter_node(initial_state)
    
    leads = result["leads"]
    for lead in leads:
        print(f"\n🏢 Company: {lead['company_name']}")
        print(f"   Score: {lead['score']}/100")
        print(f"   Status: {lead['status']}")
        print(f"   Summary: {lead['summary']}")

except Exception as e:
    print(f"\n❌ Test Failed: {e}")
    import traceback
    traceback.print_exc()
