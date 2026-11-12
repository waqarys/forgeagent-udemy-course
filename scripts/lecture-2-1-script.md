# Lecture 2.1 Script – Anatomy of the Agent Loop
**Length target:** 8–10 minutes  
**Format:** Talking head intro → screen share of code → back to face for key points.

**[0:00–1:00] Intro**  
“In the last lecture we set up the project. Today we look at the actual loop that makes Forge an agent. The whole idea fits on one slide: the agent repeatedly asks a brain what to do next, runs any tools it requests, then feeds the results back.”

**[1:00–4:00] Walk the code**  
Open `forge/full_agent.py` (or the skeleton). Highlight the `run` method.  
Explain:  
- Memory holds the conversation.  
- Each step we build context and ask the brain.  
- If the brain returns a tool call, we execute it and add the result.  
- If it returns a final answer, we stop.

**[4:00–6:30] Why this design**  
“This is deliberately simple. No hidden state machines. You can put a print statement anywhere and see exactly what the agent is thinking. Later we’ll swap the mock brain for a real LLM and add safety checks.”

**[6:30–end] Run it**  
Run the demo. Show the tool calls and the final message.  
“In the next lecture we’ll replace the mock brain with a real API call.”

**On-camera notes:** Pause after running the demo. Ask “Does this match what you expected an agent loop to look like?”
