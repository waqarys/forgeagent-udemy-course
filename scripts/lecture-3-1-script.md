# Lecture 3.1 Script – Making the First LLM Call
**Length target:** 9–12 minutes  

**[0:00–1:30] Setup**  
“Today we replace the mock brain with a real model. We’ll start with a single provider so the code stays clear.”

**[1:30–6:00] Code walkthrough**  
Show how to load the API key from `.env`.  
Demonstrate a minimal request (using `requests`).  
Explain the system prompt that tells the model it can call tools.

**[6:00–9:00] Run a real example**  
Call the agent with a simple goal. Show the actual response.  
Mention cost and rate limits briefly.

**[9:00–end] Next**  
“Next we’ll abstract the brain so you can switch providers with one line.”

**Recording tip:** Have your API key already in `.env` (or use a dummy and show the error path). Never show the full key on camera.
