from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

SQLALCHEMY_DATABASE_URL = "sqlite:///./ticketops.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def init_db():
    from app import models

    Base.metadata.create_all(bind=engine)
    db = SessionLocal()

    if db.query(models.Owner).count() == 0:
        owners = [models.Owner(name=f"Team {c}") for c in ["Alpha", "Beta", "Gamma", "Delta", "Epsilon"]]
        db.add_all(owners)
        db.commit()
        for o in owners:
            db.refresh(o)

        items = []
        for i in range(1, 41):
            items.append(models.Item(name=f"Ticket #{i}", owner_id=owners[i % len(owners)].id))
        db.add_all(items)
        db.commit()

    if db.query(models.User).count() == 0:
        db.add_all(
            [
                models.User(id=1, username="alex", role="user"),
                models.User(id=2, username="jordan", role="admin"),
            ]
        )
        db.commit()

    db.close()
