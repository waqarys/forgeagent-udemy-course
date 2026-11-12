"""Core agent loop – original implementation for the course."""
from dataclasses import dataclass
from typing import List, Optional

@dataclass
class Thought:
    text: str
    tool_calls: List[dict] = None
    is_final: bool = False

class Agent:
    def __init__(self):
        self.history: List[str] = []

    def run(self, user_goal: str) -> str:
        self.history.append(f"User: {user_goal}")
        # Placeholder loop – expanded in later lectures
        return "Hello from Forge. The real loop comes in the next section."
