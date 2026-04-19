from sqlalchemy.orm import Session
from app.models.stores import Store
from datetime import datetime
from app.schemas.stores import StoreCreate, StoreBase


def get_all_stores(db: Session):
    return db.query(Store).all()


def get_store_by_id(db: Session, store_id: str):
    return db.query(Store).filter(Store.store_id == store_id).first()


def create_store(db: Session, store: StoreCreate):
    db_store = Store(
        name=store.name,
        address=store.address,
        store_id=store.store_id,
        city=store.city,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(db_store)
    db.commit()
    db.refresh(db_store)
    return db_store


def update_store(db: Session, store_id: str, update_store: StoreBase):
    db_store = db.query(Store).filter(Store.store_id == store_id).first()
    if not db_store:
        return None
    for key, value in update_store.dict(exclude_unset=True).items():
        setattr(db_store, key, value)
    db_store.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_store)
    return db_store


def delete_store(db: Session, store_id: str):
    db_store = db.query(Store).filter(Store.store_id == store_id).first()
    if not db_store:
        return None
    db.delete(db_store)
    db.commit()
    return db_store
