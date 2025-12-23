from typing import Any, Dict
from playwright.async_api import async_playwright
from src.graph.state import LeadState

async def scrape_node(state: LeadState) -> Dict[str, Any]:
    """
    Visit the each new lead's URL and scrape text content
    """
    leads = state.get("leads")

    leads_to_scrape = [lead for lead in leads if lead.get("status") == "new"]

    if not leads_to_scrape:
        print("No new leads to scrape.")
        return {"leads": leads}
    
    scrapped_leads = []

    async with async_playwright() as p:
        "Launch  browser "
        browser = await p.chromium.launch(headless=False, args=["--ignore-certificate-errors"])
        context = await browser.new_context(ignore_https_errors=True)

        for lead in leads_to_scrape:
            url = lead.get("url")
            print(f"Scraping URL: {url}")

            try:
                page = await context.new_page()
                await page.goto(url, timeout=60000, wait_until="domcontentloaded")
                text_content = await page.inner_text("body")

                clean_text = " ".join(text_content.split())[:5000]
                lead['description'] = clean_text
                lead['status'] = 'scraped'
                scrapped_leads.append(lead)
                await page.close()
            except Exception as e:
                print(f"Error during scraping: {e}")
                lead['status'] = 'error'
                scrapped_leads.append(lead)
        await browser.close()

    return {"leads": scrapped_leads}