from src.graph.state import LeadState
from src.graph.nodes.search_node import search_node

# Simulate the input from the user
# Note: In LangGraph, state is usually a dictionary!
initial_state = {
    "search_query": "AI marketing agencies in india",
    "max_results": 3,
    "leads": [],
    "current_step": "start"
}

print("🚀 Running Search Node Test...")
try:
    result = search_node(initial_state)
    
    leads = result.get("leads", [])
    print(f"\n✅ Result returned {len(leads)} leads:")
    for i, lead in enumerate(leads, 1):
        print(f"{i}. {lead['company_name']} ({lead['url']})")
        
except Exception as e:
    print(f"\n❌ Test Failed with error:")
    print(vars(e) if hasattr(e, 'message') else e)
    import traceback
    traceback.print_exc()
