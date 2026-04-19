from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class AssetStockBase(BaseModel):
    asset_name: str
    quantity: int
    store_id: str


class AssetStockCreate(AssetStockBase):
    pass


class AssetStockResponse(AssetStockBase):
    id: int
    created_at: datetime
    updated_at: datetime


class Config:
    orm_mode = True
    from_attributes = True
