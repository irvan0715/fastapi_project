from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db.database import Base


class Store(Base):
    __tablename__ = "stores"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    name = Column(String, nullable=False)
    address = Column(String, nullable=False)
    store_id = Column(String, unique=True, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    users = relationship("User", back_populates="stores")
    tickets = relationship("Ticket", back_populates="stores")
    assets_stock = relationship("AssetsStock", back_populates="stores")
