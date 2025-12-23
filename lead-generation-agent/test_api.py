import requests
import json

url = "http://localhost:8000/api/search"
payload = {
    "query": "Gaming companies in India",
    "icp": {
        "industry": "Gaming",
        "companySize": "Small",
        "targetRegion": "India",
        "painPoints": "Hiring",
        "technologies": "Unity"
    },
    "max_results": 1
}

print(f"Testing API: {url}")
try:
    response = requests.post(url, json=payload)
    if response.status_code == 200:
        print("API Call Successful!")
        print(json.dumps(response.json(), indent=2))
    else:
        print(f"API Call Failed: {response.status_code}")
        print(response.text)
except Exception as e:
    print(f"Error connecting to API: {e}")
