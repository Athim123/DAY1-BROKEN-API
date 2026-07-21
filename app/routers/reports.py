import time
import asyncio
from fastapi import APIRouter, Depends
from app.auth import get_current_user

router = APIRouter()


def build_notes(current_user, existing_notes=None):
    if existing_notes is None:
        existing_notes = []

    existing_notes.append(f"requested by {current_user.username}")

    return existing_notes


@router.post("/summary")
async def generate_summary(current_user=Depends(get_current_user)):
    notes = build_notes(current_user)

    await asyncio.sleep(2)

    return {
        "summary": f"Report generated with {len(notes)} note(s)",
        "notes": notes,
    }
