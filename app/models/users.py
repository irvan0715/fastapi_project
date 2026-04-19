from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    username = Column(String, unique=True, index=True, nullable=False)
    # password = Column(String, nullable=False)
    hashed_password = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    is_admin = Column(Integer, nullable=False, default=0)
    phone = Column(String, unique=True, nullable=False)
    full_name = Column(String, index=True, nullable=False)
    employee_no = Column(String, unique=True, index=True, nullable=False)
    department = Column(String, index=True, nullable=False)
    city = Column(String, index=True, nullable=False)
    store_id = Column(String, ForeignKey("stores.store_id"), index=True, nullable=False)
    is_active = Column(Integer, nullable=False, default=1)
    created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)

    stores = relationship("Store", back_populates="users")
    tickets = relationship("Ticket", back_populates="users")
