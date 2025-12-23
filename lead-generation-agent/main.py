from src.graph.workflow import create_workflow
from dotenv import load_dotenv

load_dotenv()

def main():
    print("Agent intializing...")

    # query = input("Enter your query: ")
    print("\n--- Enter Lead Criteria ---")
    industry = input("Enter Industry Type (e.g. Gaming, Fintech): ")
    territory = input("Enter Territory/Location (e.g. India, US): ")
    firm_size = input("Enter Firm Size (e.g. Small, Medium, Enterprise) [Optional]: ")
    tech_stack = input("Enter Tech Stack (e.g. Unity, React) [Optional]: ")
    pain_points = input("Enter Pain Points (e.g. Hiring cost, Legacy systems) [Optional]: ")
    max_results = int(input("Enter max results (e.g. 5): "))
    
    app = create_workflow()

    intial_state = {
        "search_query": "", # Will be constructed in search_node
        "max_results": max_results,
        "leads" : [],
        "industry": industry,
        "territory": territory,
        "firm_size": firm_size,
        "tech_stack": tech_stack,
        "pain_points": pain_points,
    }

    print("\n Starting workflow ... (this may take a minute)")

    print("=="*50)

    try:
        result = app.invoke(intial_state)

        leads = result.get("leads", [])
        print("\n Workflow completed successfully.")
        print("=="*50)

        for i, lead in enumerate(leads,1):
            print(f"\n Lead {i+1}")
            print(f"   Company: {lead['company_name']}")
            print(f"   Status: {lead['status']}")

            if lead['status'] == "pitched":
                print(f" email: {lead.get('email','NA')}")
                print(f" summary: {lead.get('summary','NA')}")
                print(f" pitch: {lead.get('pitch','NA')}")

    except Exception as e:
        print(f"\n Error during workflow: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    main()