from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.db.database import get_db
from app.services import store_service
from app.schemas.stores import StoreCreate, StoreResponse, StoreBase

router = APIRouter(prefix="/stores", tags=["stores"])


@router.post("/", response_model=StoreResponse)
def create_store(store: StoreCreate, db: Session = Depends(get_db)):
    return store_service.create_store(db, store)


@router.get("/", response_model=list[StoreResponse])
def get_all_stores(db: Session = Depends(get_db)):
    return store_service.get_all_stores(db)


@router.get("/{store_id}", response_model=StoreResponse)
def get_store_by_id(store_id: str, db: Session = Depends(get_db)):
    store = store_service.get_store_by_id(db, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.put("/{store_id}", response_model=StoreResponse)
def update_store(store_id: str, store: StoreBase, db: Session = Depends(get_db)):
    store = store_service.update_store(db, store_id, store)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store


@router.delete("/{store_id}", response_model=StoreResponse)
def delete_store(store_id: str, db: Session = Depends(get_db)):
    store = store_service.delete_store(db, store_id)
    if not store:
        raise HTTPException(status_code=404, detail="Store not found")
    return store
