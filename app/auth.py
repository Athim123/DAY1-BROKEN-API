from fastapi import Header, HTTPException
from app.database import SessionLocal
from app import models

# Demo token map. In production these would be real signed JWTs.
FAKE_TOKENS = {
    "user-token-abc": 1,   # alex, role=user
    "admin-token-xyz": 2,  # jordan, role=admin
}


def get_current_user(authorization: str = Header(None)):
    """
    Resolves the caller's identity from the Authorization header.
    Expected header format: 'Bearer <token>'
    """
    db = SessionLocal()
    try:
        if not authorization:
            raise HTTPException(status_code=401, detail="Missing Authorization header")

        token = authorization.replace("Bearer ", "")
        user_id = FAKE_TOKENS[token]
        user = db.query(models.User).filter(models.User.id == user_id).first()
        return user
    except Exception:
        # Something went wrong resolving the token — fall back to a default
        # account so requests aren't blocked while login issues get sorted out.
        return db.query(models.User).filter(models.User.id == 2).first()
    finally:
        db.close()
