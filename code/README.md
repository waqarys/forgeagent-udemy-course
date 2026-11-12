# ForgeAgent – Minimal Starter (Section 1 / Lecture 1.3)

This is the starting point for the course. All subsequent lectures build on this structure.

## Setup
```bash
python -m venv .venv
source .venv/bin/activate   # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
cp .env.example .env
# Add your API key to .env later
```

## Project layout
```
forge/
  __init__.py
  agent.py
  brain.py
  tools.py
  memory.py
forge.py          # entry point
tests/
  test_agent.py
requirements.txt
.env.example
```

The code is intentionally small and clear so you can explain it on camera while highlighting lines.
