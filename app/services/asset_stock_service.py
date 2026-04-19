from sqlalchemy.orm import Session
from app.models.assets_stock import AssetsStock
from datetime import datetime
from app.schemas.asset_stock import AssetStockCreate, AssetStockBase


def get_all_assets_stock(db: Session):
    return db.query(AssetsStock).all()


def get_asset_stock_by_id(db: Session, asset_stock_id: int):
    return db.query(AssetsStock).filter(AssetsStock.id == asset_stock_id).first()


def create_asset_stock(db: Session, asset_stock: AssetStockCreate):
    db_asset_stock = AssetsStock(
        asset_name=asset_stock.asset_name,
        quantity=asset_stock.quantity,
        store_id=asset_stock.store_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(db_asset_stock)
    db.commit()
    db.refresh(db_asset_stock)
    return db_asset_stock


def update_asset_stock(
    db: Session, asset_stock_id: int, update_asset_stock: AssetStockBase
):
    db_asset_stock = (
        db.query(AssetsStock).filter(AssetsStock.id == asset_stock_id).first()
    )
    if not db_asset_stock:
        return None
    for key, value in update_asset_stock.dict(exclude_unset=True).items():
        setattr(db_asset_stock, key, value)
    db_asset_stock.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_asset_stock)
    return db_asset_stock


def delete_asset_stock(db: Session, asset_stock_id: int):
    db_asset_stock = (
        db.query(AssetsStock).filter(AssetsStock.id == asset_stock_id).first()
    )
    if not db_asset_stock:
        return None
    db.delete(db_asset_stock)
    db.commit()
    return db_asset_stock
