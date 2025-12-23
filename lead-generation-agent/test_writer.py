from src.graph.nodes.write_node import write_node
from dotenv import load_dotenv

load_dotenv()

# Mock State with a qualified lead
initial_state = {
    "leads": [
        {
            "company_name": "RetailAI Solutions",
            "url": "https://retail-ai.com",
            "description": "RetailAI uses computer vision to track inventory in real-time for large grocery chains. Our system reduces waste by 30%.",
            "summary": "Computer vision for grocery inventory tracking.",
            "status": "qualified",
            "score": 92,
            "email": "info@retail-ai.com"
        }
    ]
}

print("✍️ Running Writer Node Test...")
try:
    result = write_node(initial_state)
    
    leads = result["leads"]
    for lead in leads:
        print(f"\n🏢 {lead['company_name']}")
        print(f"   Status: {lead['status']}")
        print(f"   Pitch Preview:\n{'-'*40}")
        print(f"{lead.get('pitch', 'No pitch')}")
        print(f"{'-'*40}")

except Exception as e:
    print(f"\n❌ Test Failed: {e}")
    import traceback
    traceback.print_exc()
