from fastapi import Header, HTTPException,status
from app.database import SessionLocal
from app import models


# Demo token map. In production these would be real signed JWTs.
FAKE_TOKENS = {
    "user-token-abc": 1,   # alex, role=user
    "admin-token-xyz": 2,  # jordan, role=admin
}


def get_current_user(authorization: str = Header(None)):
    db = SessionLocal()

    try:
        if authorization is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Missing Authorization header",
            )

        if not authorization.startswith("Bearer "):
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid authorization format",
            )

        token = authorization.removeprefix("Bearer ").strip()

        user_id = FAKE_TOKENS.get(token)

        if user_id is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Invalid token",
            )

        user = db.query(models.User).filter(models.User.id == user_id).first()

        if user is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User not found",
            )

        return user

    finally:
        db.close()
