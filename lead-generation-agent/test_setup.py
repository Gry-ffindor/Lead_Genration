from langchain_groq import ChatGroq
from duckduckgo_search import DDGS
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

def test_environment():
    print("🧪 Testing Setup...")
    
    # 1. Test API Key Presence
    api_key = os.getenv("GROQ_API_KEY")
    if not api_key:
        print("❌ Error: GROQ_API_KEY not found in .env file")
        return

    # 2. Test LLM Connection
    print("   Checking LLM connection (Groq)...")
    try:
        llm = ChatGroq(model_name="llama-3.3-70b-versatile", temperature=0)
        response = llm.invoke("Say 'Hello'")
        print(f"   ✅ LLM Success! Response: {response.content}")
    except Exception as e:
        print(f"   ❌ LLM Failed: {e}")

    # 3. Test Search Tool
    print("   Checking Search Tool (DuckDuckGo)...")
    try:
        results = DDGS().text("LangGraph framework", max_results=1)
        if results:
            print(f"   ✅ Search Success! Found: {results[0]['title']}")
        else:
            print("   ⚠️ Search returned no results (but connected)")
    except Exception as e:
        print(f"   ❌ Search Failed: {e}")

if __name__ == "__main__":
    test_environment()
