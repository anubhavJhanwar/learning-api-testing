from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from config import DATABASE_URL

# Create the SQLAlchemy engine (pool_pre_ping checks connection health)
engine = create_engine(DATABASE_URL, pool_pre_ping=True)

# Each request gets its own session
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base class for all ORM models
Base = declarative_base()


def get_db():
    """Dependency that provides a DB session per request, then closes it."""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
