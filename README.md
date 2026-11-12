# ForgeAgent Udemy Course Materials

Original course content for **Building a Coding Agent from Scratch in Pure Python**.

## Repository Structure
- `docs/` — Course outline, OBS guide, completion checklist
- `scripts/` — Talking-head scripts for key lectures
- `code/` — Runnable starter code + fuller demo agent (`forge/full_agent.py`)
- `obs/` — OBS Studio scene collection (import directly)
- `slides/` — Slide deck structures

## Quick Start
```bash
cd code
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python -m forge.full_agent   # runs the demo agent
pytest
```

## Recording
1. Import `obs/forgeagent-scenes.json` into OBS.
2. Install the background-removal plugin and assign your camera.
3. Use the scripts in `scripts/` — they are written for your own voice and camera.
4. All code is pre-written and runnable; highlight or paste blocks while you narrate.

All materials are original and written specifically for this course.
