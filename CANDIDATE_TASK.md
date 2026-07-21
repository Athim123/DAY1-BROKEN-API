# Day 1 Task — Fix the TicketOps API

## What this is

`TicketOps API` is a small FastAPI service with three endpoints. It runs, but it has
**3–4 real bugs** hiding in it the kind that pass a quick manual test but cause
problems in production (security issues, performance issues, subtle state bugs).

Your job today is to find them, fix them, and be ready to explain what you did.

## Setup

```bash
python -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Once it's running, open http://127.0.0.1:8000/docs for interactive API docs, or use
curl / Postman.

Endpoints:
- `GET /health` — basic health check
- `GET /items/` — list all tickets with their owning team
- `POST /reports/summary` — generate a report summary

Auth is via header: `Authorization: Bearer user-token-abc` (regular user) or
`Authorization: Bearer admin-token-xyz` (admin). Try requests with a valid token,
an invalid token, and no token at all — pay attention to what each one actually
returns.

## What to do

1. **Find the bugs.** Read the code, run the service, poke at it with different
   inputs. Don't assume there's exactly one bug per file.
2. **Fix them.** Make a git commit for each distinct fix, with a message
   explaining what was wrong and why your fix addresses it. (Incremental commits
   — not one giant commit at the end.)
3. **Write a short note (in `NOTES.md`, create it) for each bug**, in your own
   words:
   - What was actually happening
   - Why it's a problem 
   - What you changed and why that's the right fix
4. Push your work to a git repo and be ready to walk through it
   live this afternoon.

## What we're looking for

- Whether you can actually find bugs by reading and testing code, not just
  running a linter
- Whether your fixes are correct and don't introduce new problems
- Whether you can explain *why* something was broken, not just that it's fixed
  now
- How you work do you test as you go, commit sensibly, and reason about
  what could break at scale


## This afternoon

We'll do a live walkthrough: you'll share your screen, walk through each bug
and fix, and I'll ask questions and may ask you to make a small change on the
spot. Bring your own reasoning, not just the final diff.
