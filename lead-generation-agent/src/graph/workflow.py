from langgraph.graph import StateGraph, END
from src.graph.nodes.search_node import search_node
from src.graph.nodes.filter_node import filter_node
from src.graph.nodes.scrape_node import scrape_node
from src.graph.nodes.email_node import email_node
from src.graph.nodes.write_node import write_node
from src.graph.state import LeadState   


def create_workflow():
    graph = StateGraph(LeadState)

    graph.add_node("search", search_node)
    graph.add_node("filter", filter_node)
    graph.add_node("scrape", scrape_node)
    graph.add_node("email", email_node)
    graph.add_node("write", write_node)

    graph.set_entry_point("search")
    graph.add_edge("search", "scrape")
    graph.add_edge("scrape", "filter")
    graph.add_edge("filter", "email")
    graph.add_edge("email", "write")
    graph.add_edge("write", END)

    app = graph.compile()
    return app


