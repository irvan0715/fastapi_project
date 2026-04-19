from fastapi import FastAPI
from app.db.database import engine, Base
import app.models
from app.api import ticket, user, store, asset_stock, auth

app = FastAPI()

Base.metadata.create_all(bind=engine)

app.include_router(ticket.router)
app.include_router(user.router)
app.include_router(store.router)
app.include_router(asset_stock.router)
app.include_router(auth.router)
