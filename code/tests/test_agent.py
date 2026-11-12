def test_agent_starts():
    from forge.agent import Agent
    agent = Agent()
    result = agent.run("test")
    assert "Forge" in result
