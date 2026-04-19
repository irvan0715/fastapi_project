from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class StoreBase(BaseModel):
    name: str
    address: str
    store_id: str
    city: str


class StoreCreate(BaseModel):
    name: str
    address: str
    store_id: str
    city: str


class StoreResponse(StoreBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Config:
    orm_mode = True
    from_attributes = True
