from google.adk.tools.tool_context import ToolContext
from typing import List

def save_attractions_to_state(
    tool_context: ToolContext,
    attractions: List[str]
) -> dict[str, str]:
    """
    Saves the list of attractions to the state["attractions"]

        Args:
          attractions[str]: a list of strings to add to the list of attractions
        
        Returns:
          dict of status {"status": "success"}
    """
    existing_attractions = tool_context.state.get("attractions", [])
    tool_context.state["attractions"] = existing_attractions + attractions
    return {"status": "success"}
