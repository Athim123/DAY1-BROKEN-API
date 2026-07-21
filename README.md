# TicketOps API

Start here: **[CANDIDATE_TASK.md](./CANDIDATE_TASK.md)**

## Project structure

```
app/
  main.py              FastAPI app + router registration
  database.py          SQLite + SQLAlchemy setup, seed data
  models.py            User / Owner / Item models
  auth.py               Auth dependency
  routers/
    items.py           GET /items/
    reports.py          POST /reports/summary
requirements.txt
```
