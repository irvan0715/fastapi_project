from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import asset_stock_service
from app.schemas.asset_stock import AssetStockCreate, AssetStockResponse, AssetStockBase

router = APIRouter(prefix="/assets_stock", tags=["assets_stock"])


@router.post("/", response_model=AssetStockResponse)
def create_asset_stock(asset_stock: AssetStockCreate, db: Session = Depends(get_db)):
    return asset_stock_service.create_asset_stock(db, asset_stock)


@router.get("/", response_model=list[AssetStockResponse])
def get_all_assets_stock(db: Session = Depends(get_db)):
    return asset_stock_service.get_all_assets_stock(db)


@router.get("/{asset_stock_id}", response_model=AssetStockResponse)
def get_asset_stock_by_id(asset_stock_id: int, db: Session = Depends(get_db)):
    asset_stock = asset_stock_service.get_asset_stock_by_id(db, asset_stock_id)
    if not asset_stock:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset_stock


@router.put("/{asset_stock_id}", response_model=AssetStockResponse)
def update_asset_stock(
    asset_stock_id: int, asset_stock: AssetStockBase, db: Session = Depends(get_db)
):
    asset_stock = asset_stock_service.update_asset_stock(
        db, asset_stock_id, asset_stock
    )
    if not asset_stock:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset_stock


@router.delete("/{asset_stock_id}", response_model=AssetStockResponse)
def delete_asset_stock(asset_stock_id: int, db: Session = Depends(get_db)):
    asset_stock = asset_stock_service.delete_asset_stock(db, asset_stock_id)
    if not asset_stock:
        raise HTTPException(status_code=404, detail="Asset not found")
    return asset_stock
