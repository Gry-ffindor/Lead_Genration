from playwright.sync_api import sync_playwright

url = "https://builtin.com/articles/gaming-companies-in-india"

print(f"Testing scrape for: {url}")

with sync_playwright() as p:
    print("Launching browser...")
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    try:
        print("Navigating...")
        # Matching the new implementation
        page.goto(url, timeout=60000, wait_until="domcontentloaded")
        print("Page loaded.")
        text_content = page.inner_text("body")
        print(f"Extracted {len(text_content)} characters.")
    except Exception as e:
        print(f"Scrape failed: {e}")
    finally:
        browser.close()
