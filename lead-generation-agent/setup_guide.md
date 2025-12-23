# Phase 1: Setup & Initialization Guide

Great choice to build this yourself! I've set up the folder structure for you. Here is your checklist to get the environment ready.

## 1. Environment Setup

Open your terminal in the `lead-generation-agent` folder:

```bash
cd lead-generation-agent
```

Create a virtual environment (recommended):

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

Install the dependencies I defined in `pyproject.toml` (using pip):

```bash
pip install -e .
```

## 2. Install Playwright Browsers

We need the actual browser binaries for the scraper to work:

```bash
playwright install chromium
```

## 3. Configure API Keys

1.  **Groq (for LLM)**: Go to [Groq Console](https://console.groq.com/keys), sign up (it's free), and create an API Key.
2.  **LangSmith (Optional)**: If you want to visualize the graph, get a key from [Smith.LangChain.com](https://smith.langchain.com/).

Copy the example env file and edit it:

```bash
cp .env.example .env
# Now open .env in your editor and paste your keys
```

## 4. Verify Setup

Create a quick test file `test_setup.py` to make sure everything works:

```python
from langchain_groq import ChatGroq
from duckduckgo_search import DDGS
from dotenv import load_dotenv
import os

load_dotenv()

def test_environment():
    print("Testing dependencies...")

    # 1. Test LLM
    try:
        llm = ChatGroq(model_name="llama3-8b-8192")
        response = llm.invoke("Say 'Hello World'")
        print(f"✅ LLM Check: {response.content}")
    except Exception as e:
        print(f"❌ LLM Check Failed: {e}")

    # 2. Test Search
    try:
        results = DDGS().text("LangGraph framework", max_results=1)
        print(f"✅ Search Check: Found {len(results)} result")
    except Exception as e:
        print(f"❌ Search Check Failed: {e}")

if __name__ == "__main__":
    test_environment()
```

Run it:

```bash
python test_setup.py
```

---

**Next Step**: Once you see two green checks ✅, tell me, and we'll move to **Phase 2: Building the Web Scraper Node**.
