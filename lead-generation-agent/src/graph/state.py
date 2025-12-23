import operator
from typing import Annotated, List, TypedDict

class Lead(TypedDict):
    "Respresents a lead with basic information."
    company_name: str
    url: str
    description: str
    score: int
    email: str
    summary: str
    pitch:str
    status: str 

class LeadState(TypedDict):
    "Global state of graph"
    search_query: str
    max_results: int
    leads: List[Annotated[Lead, "List of leads"]]
    current_step: str
    industry: str
    territory: str
    firm_size: str
    tech_stack: str
    pain_points: str