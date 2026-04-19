from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db.database import Base


class AssetsStock(Base):
    __tablename__ = "assets_stock"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    asset_name = Column(String, index=True, nullable=False)
    quantity = Column(Integer, nullable=False)
    store_id = Column(String, ForeignKey("stores.store_id"), index=True, nullable=False)
    created_at = Column(String, nullable=False)
    # updated_at = Column(String, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(String, nullable=False)

    stores = relationship("Store", back_populates="assets_stock")
