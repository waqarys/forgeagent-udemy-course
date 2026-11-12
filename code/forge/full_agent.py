"""
ForgeAgent – Working implementation for the course.
Original pure-Python coding agent (no frameworks).

This version includes:
- Basic control loop
- Simple file tools
- In-memory conversation history
- Placeholder for plan mode and persistent memory

Expand in later sections as shown in the scripts.
"""
import os
import json
from dataclasses import dataclass, field
from typing import List, Dict, Any, Optional
from pathlib import Path

@dataclass
class Message:
    role: str  # "user", "assistant", "tool"
    content: str
    tool_call_id: Optional[str] = None

class SimpleMemory:
    def __init__(self):
        self.messages: List[Message] = []

    def add(self, role: str, content: str, tool_call_id: Optional[str] = None):
        self.messages.append(Message(role, content, tool_call_id))

    def get_context(self, max_messages: int = 20) -> str:
        recent = self.messages[-max_messages:]
        lines = []
        for m in recent:
            lines.append(f"{m.role.upper()}: {m.content}")
        return "\n".join(lines)

class ToolRegistry:
    def __init__(self, workspace: str = "."):
        self.workspace = Path(workspace).resolve()

    def list_files(self, path: str = ".") -> str:
        target = (self.workspace / path).resolve()
        if not str(target).startswith(str(self.workspace)):
            return "Error: path outside workspace"
        try:
            items = [p.name for p in target.iterdir()]
            return "\n".join(items) if items else "(empty)"
        except Exception as e:
            return f"Error: {e}"

    def read_file(self, path: str) -> str:
        target = (self.workspace / path).resolve()
        if not str(target).startswith(str(self.workspace)):
            return "Error: path outside workspace"
        try:
            return target.read_text(encoding="utf-8")[:8000]
        except Exception as e:
            return f"Error: {e}"

    def write_file(self, path: str, content: str) -> str:
        target = (self.workspace / path).resolve()
        if not str(target).startswith(str(self.workspace)):
            return "Error: path outside workspace"
        try:
            target.parent.mkdir(parents=True, exist_ok=True)
            target.write_text(content, encoding="utf-8")
            return f"Wrote {len(content)} characters to {path}"
        except Exception as e:
            return f"Error: {e}"

    def execute(self, name: str, args: Dict[str, Any]) -> str:
        if name == "list_files":
            return self.list_files(args.get("path", "."))
        if name == "read_file":
            return self.read_file(args.get("path", ""))
        if name == "write_file":
            return self.write_file(args.get("path", ""), args.get("content", ""))
        return f"Unknown tool: {name}"

class ForgeAgent:
    def __init__(self, workspace: str = "."):
        self.memory = SimpleMemory()
        self.tools = ToolRegistry(workspace)
        self.mode = "act"  # "plan" or "act"

    def run(self, user_goal: str, max_steps: int = 8) -> str:
        self.memory.add("user", user_goal)
        for step in range(max_steps):
            context = self.memory.get_context()
            # In a real lecture we replace this with an actual LLM call
            response = self._mock_brain(context, step)
            self.memory.add("assistant", response)
            if "FINAL:" in response:
                return response.split("FINAL:", 1)[1].strip()
            # Simple tool parsing for demo
            if "TOOL:" in response:
                try:
                    tool_line = response.split("TOOL:", 1)[1].strip()
                    name, arg_json = tool_line.split("|", 1)
                    args = json.loads(arg_json)
                    result = self.tools.execute(name.strip(), args)
                    self.memory.add("tool", result)
                except Exception as e:
                    self.memory.add("tool", f"Tool error: {e}")
        return "Stopped after max steps. Check memory for details."

    def _mock_brain(self, context: str, step: int) -> str:
        # Demo brain so the starter runs without an API key.
        # Replace with real provider calls in Section 3.
        if step == 0:
            return "TOOL: list_files|{\"path\": \".\"}"
        if step == 1:
            return "TOOL: read_file|{\"path\": \"README.md\"}"
        return "FINAL: Demo complete. In the real course the brain is an LLM that decides the next tool or final answer."

if __name__ == "__main__":
    agent = ForgeAgent()
    print(agent.run("Explore the current directory and summarize what you see."))
