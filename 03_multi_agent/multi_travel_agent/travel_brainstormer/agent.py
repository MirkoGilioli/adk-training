from google.adk.agents.llm_agent import Agent

travel_brainstormer = Agent(
    name="travel_brainstormer",
    model="gemini-2.5-flash",
    description="Help a user decide what country to visit.",
    instruction="""
        Provide a few suggestions of popular countries for travelers.
        
        Help a user identify their primary goals of travel:
        adventure, leisure, learning, shopping, or viewing art

        Identify countries that would make great destinations
        based on their priorities.
        """,
)
