"""Minimal agent entry point for the first lectures."""
from forge.agent import Agent

def main():
    agent = Agent()
    result = agent.run("Say hello and stop.")
    print(result)

if __name__ == "__main__":
    main()
