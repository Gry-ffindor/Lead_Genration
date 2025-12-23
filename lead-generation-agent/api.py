from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import List, Optional
from src.graph.workflow import create_workflow
from dotenv import load_dotenv
import uuid

load_dotenv()


app = FastAPI(title="Lead Generation Agent API")

# Configure CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://localhost:3000"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class ICP(BaseModel):
    industry: str
    companySize: str
    targetRegion: str
    painPoints: str
    technologies: str

class SearchRequest(BaseModel):
    query: str
    icp: ICP
    max_results: int = 5

class LeadResponse(BaseModel):
    id: str
    name: str
    website: str
    industry: str
    size: str
    summary: str
    email: str
    pitch: str
    sources: List[dict]
    status: str

@app.post("/api/search", response_model=List[LeadResponse])
async def search_leads(request: SearchRequest):
    try:
        print(f"Received search request: {request}")
        app_workflow = create_workflow()
        
        # Map request to agent state
        initial_state = {
            "search_query": request.query,
            "max_results": request.max_results,
            "leads": [],
            "industry": request.icp.industry,
            "territory": request.icp.targetRegion,
            "firm_size": request.icp.companySize,
            "tech_stack": request.icp.technologies,
            "pain_points": request.icp.painPoints
        }
        
        print(f"Invoking workflow with state: {initial_state}")
        result = await app_workflow.ainvoke(initial_state)
        
        agent_leads = result.get("leads", [])
        print(f"Workflow finished. Found {len(agent_leads)} leads.")
        
        # Map agent leads to frontend definition
        mapped_leads = []
        for lead in agent_leads:
            mapped_leads.append({
                "id": str(uuid.uuid4()),
                "name": lead.get("company_name", "Unknown"),
                "website": lead.get("url", "#"),
                "industry": request.icp.industry, # Fallback
                "size": request.icp.companySize, # Fallback
                "summary": lead.get("summary") or lead.get("description") or "No summary available.",
                "email": lead.get("email", ""),
                "pitch": lead.get("pitch", "No pitch generated."),
                "sources": [{"title": "Source", "uri": lead.get("url", "#")}], 
                "status": "new"
            })
            
        return mapped_leads

    except Exception as e:
        print(f"Error processing request: {e}")
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
