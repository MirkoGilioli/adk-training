from google.adk.agents.llm_agent import Agent
from google.adk.tools.tool_context import ToolContext
from typing import List

def save_attractions_to_state(
    tool_context: ToolContext,
    attractions: List[str]
) -> dict[str, str]:
    """Saves a list of attractions to the tool context state.

    Args:
        tool_context (ToolContext): The context for the tool, providing access to state.
        attractions (List[str]): A list of attraction names to add to the state.

    Returns:
        dict[str, str]: A dictionary indicating the status of the operation.
    """
    existing_attractions = tool_context.state.get("attractions", [])
    tool_context.state["attractions"] = existing_attractions + attractions
    return {"status": "success"}
    

attractions_planner = Agent(
    model='gemini-2.5-flash',
    name='attractions_planner',
    description="Build a list of attractions for a given destination.",
    instruction="""
        - Build a list of attractions for a given destination by the user
        - When the user reply with a given list of attractions, use your tools to save their selected attractions
        - If User ask about what attractions has chosen, provide the list of {{ "attractions" }}
        """,
    tools=[
        save_attractions_to_state
    ]
)
