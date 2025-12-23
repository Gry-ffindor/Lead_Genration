from ddgs import DDGS
import importlib.metadata

try:
    version = importlib.metadata.version("duckduckgo-search")
    print(f"duckduckgo-search version: {version}")
except Exception as e:
    print(f"Could not get duckduckgo-search version: {e}")

try:
    version = importlib.metadata.version("ddgs")
    print(f"ddgs version: {version}")
except Exception as e:
    print(f"Could not get ddgs version: {e}")

print("Attempting search...")
try:
    print("Testing search with region='wt-wt' and corrected spelling...")
    results = DDGS().text("AI startups in Bangalore", max_results=5, region="wt-wt")
    print(f"Results (wt-wt): {results}")
except Exception as e:
    print(f"Search failed: {e}")
