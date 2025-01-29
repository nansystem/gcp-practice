from sqlalchemy.orm import sessionmaker

from app.core.config.config import settings

SessionLocal = sessionmaker(
    autocommit=False, autoflush=False, bind=settings.database_engine
)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
