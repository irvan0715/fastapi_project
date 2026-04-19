from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


class UserBase(BaseModel):
    username: str
    email: EmailStr
    phone: str
    full_name: str
    employee_no: str
    department: str
    is_admin: int
    city: str
    store_id: str
    is_active: Optional[int] = 1


class UserCreate(UserBase):
    password: str


class UserResponse(UserBase):
    id: int
    is_admin: int
    created_at: datetime
    updated_at: datetime


class Config:
    orm_mode = True
    from_attributes = True
