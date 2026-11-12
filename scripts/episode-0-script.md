# Episode 0 / Lecture 1.1 Script
## Why Build Your Own Agent in 2026?
**Format:** Talking head (your camera + voice) + occasional slides or screen.  
**Target length:** 7–9 minutes  
**Style note:** Speak naturally. Pause after key points. No voiceover — this is you on camera.

---

**[0:00 – 0:45] Hook (looking at camera)**  
“Hey, I’m [Your Name]. If you’ve tried LangChain or any of the big agent frameworks and felt like the magic was hiding more than it was helping, this course is for you.  

In the next few hours we’re going to build a complete AI coding agent from scratch in pure Python. No frameworks. No black boxes. Just a loop, some tools, and code you can actually debug. By the end you’ll have something that can read your files, edit them, run commands, and even build small projects for you.”

**[0:45 – 2:15] The problem with frameworks**  
“Most demos skip the hard parts. They show the happy path and then the agent starts deleting files or looping forever.  

The reason is simple: an agent is mostly a while loop that keeps asking a language model ‘what should I do next?’ and then runs whatever tools the model asks for. Once you own that loop, you can change anything — the memory, the safety rules, the tools, the model — without fighting a framework.”

**[2:15 – 4:00] What we will actually build**  
“We’re calling the agent Forge. By the last section it will be able to:  
- Read and edit files in a project  
- Run shell commands and react to the output  
- Keep context across turns and even across sessions  
- Switch between planning and acting modes  
- Work with both cloud models and local models through Ollama  

And you’ll have the full source code, runnable at every stage.”

**[4:00 – 6:00] How the course is structured**  
“Each section leaves you with a working version of Forge. We’ll start with the absolute minimum loop, add a brain, add tools, add memory, then put it all together in a capstone where the agent builds something useful.  

Everything is original code written for this course. You’ll also get the OBS scene collection I use so you can record your own versions or follow along cleanly.”

**[6:00 – 7:30] Who this is for & what you need**  
“This is for intermediate Python developers. If you can write a class, use a virtual environment, and make an HTTP request, you’re ready.  

You’ll need a free or paid API key for at least one provider to start (we’ll show how to swap later), and optionally Ollama if you want to run models locally. All the code is on GitHub — link is in the resources.”

**[7:30 – end] Close**  
“In the next lecture I’ll show you exactly what the finished agent looks like and how the rest of the course is organized. Then we’ll set up the project together.  

If you’re ready to stop treating agents as magic and start owning the loop, let’s get into it.”

---

**Recording tips:**  
- Look at the camera, not the screen, for the first 90 seconds.  
- Smile lightly on the hook.  
- Keep energy conversational.  
- End with a clear hand-off to the next lecture.
