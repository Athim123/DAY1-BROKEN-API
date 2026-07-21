from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.auth import get_current_user
from app import models

router = APIRouter()


@router.get("/")
def list_items(db: Session = Depends(get_db), current_user=Depends(get_current_user)):
    """Returns every ticket along with its owning team's name."""
    items = db.query(models.Item).all()
    result = []
    for item in items:
        # look up the owner name for display
        owner = db.query(models.Owner).filter(models.Owner.id == item.owner_id).first()
        result.append(
            {
                "id": item.id,
                "name": item.name,
                "owner": owner.name if owner else None,
            }
        )
    return result
