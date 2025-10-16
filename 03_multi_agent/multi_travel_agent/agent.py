from google.adk.agents.llm_agent import Agent
from .travel_brainstormer.agent import travel_brainstormer
from .attractions_planner.agent import attractions_planner


root_agent = Agent(
    name="steering",
    model="gemini-2.5-flash",
    description="Start a user on a travel adventure.",
    instruction="""
        Ask the user if they know where they'd like to travel
        or if they need some help deciding.
        If they need help deciding, send them to 'travel_brainstormer' agent.
        If they know where they'd like to travel, send them to 'attractions_planner' agent.
        Do not recommend any travel plans or suggestions to final users.
        """,
    sub_agents=[
        travel_brainstormer,
        attractions_planner
    ]
)
