from google.adk.agents.llm_agent import Agent


wiki_agent = Agent(
    name="wiki_agent",
    model="gemini-2.5-flash",
    description="You are an expert Turist Guide, and your role is to provide turistic information",
    instruction="""
        For each {{ attractions ?}} build a short tour guide given your knowledge
    """
)
