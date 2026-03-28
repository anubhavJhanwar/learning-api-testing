from pydantic import BaseModel, EmailStr, Field
from typing import Optional


class UserCreate(BaseModel):
    """Schema for creating a new user (request body)."""
    name: str = Field(..., min_length=1, max_length=100, example="Alice Smith")
    email: EmailStr = Field(..., example="alice@example.com")
    age: int = Field(..., gt=0, lt=150, example=28)


class UserUpdate(BaseModel):
    """Schema for updating a user — all fields are optional."""
    name: Optional[str] = Field(None, min_length=1, max_length=100, example="Alice Johnson")
    email: Optional[EmailStr] = Field(None, example="alice.j@example.com")
    age: Optional[int] = Field(None, gt=0, lt=150, example=29)


class UserResponse(BaseModel):
    """Schema for returning user data in responses."""
    id: int
    name: str
    email: str
    age: int

    class Config:
        from_attributes = True  # Allows ORM model -> Pydantic conversion
