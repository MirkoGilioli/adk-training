from google.adk.agents.llm_agent import Agent
from .tools import save_attractions_to_state
    

attractions_planner = Agent(
    model='gemini-2.5-flash',
    name='attractions_planner',
    description="Build a list of attractions for a given destination.",
    instruction="""
        - Build a list of attractions for a given destination by the user
        - When the user reply with a given list of attractions, use your 'save_attractions_to_state' tool to save their selected attractions
        """,
    tools=[
        save_attractions_to_state
    ]
)
