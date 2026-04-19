from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship, Mapped, mapped_column
from datetime import datetime
from app.db.database import Base


class Ticket(Base):
    __tablename__ = "tickets"

    id = Column(Integer, autoincrement=True, primary_key=True, index=True)
    ticket_no = Column(String, index=True, nullable=False)
    description = Column(String, index=True, nullable=False)
    ticket_type = Column(String, index=True, nullable=False)
    status = Column(String, index=True, nullable=False)
    ticket_owner = Column(Integer, ForeignKey("users.id"), index=True, nullable=False)
    store_id = Column(String, ForeignKey("stores.store_id"), index=True, nullable=False)
    created_at = Column(DateTime, nullable=False)
    # updated_at = Column(DateTime, nullable=False)
    updated_at: Mapped[datetime] = mapped_column(DateTime, nullable=False)
    resolved_at: Mapped[datetime] = mapped_column(DateTime, nullable=True)

    users = relationship("User", back_populates="tickets")
    stores = relationship("Store", back_populates="tickets")
