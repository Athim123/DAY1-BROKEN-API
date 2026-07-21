import time
from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter()


def build_notes(current_user, existing_notes=[]):
    """Appends an audit note for who requested this report."""
    existing_notes.append(f"requested by {current_user.username}")
    return existing_notes


@router.post("/summary")
async def generate_summary(current_user=Depends(get_current_user)):
    """
    Generates a 'summary report' — simulates calling out to a slow
    report-generation service (or an LLM provider) that takes a couple
    seconds to respond.
    """
    notes = build_notes(current_user)
    time.sleep(2)  # simulates the slow external call
    return {"summary": f"Report generated with {len(notes)} note(s) on file", "notes": notes}
