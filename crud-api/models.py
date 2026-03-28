from sqlalchemy import Column, Integer, String
from database import Base


class User(Base):
    """SQLAlchemy ORM model — maps to the 'users' table in MySQL."""
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    email = Column(String(150), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=False)
