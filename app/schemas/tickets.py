from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class TicketCreate(BaseModel):
    ticket_no: str
    description: str
    ticket_type: str
    status: str
    ticket_owner: int
    store_id: str


class TicketResponse(BaseModel):
    id: int
    ticket_no: str
    description: str
    ticket_type: str
    status: str
    ticket_owner: int
    store_id: str
    created_at: datetime
    updated_at: datetime
    resolved_at: Optional[datetime] = None


class UpdateTicket(BaseModel):
    ticket_no: Optional[str] = None
    description: Optional[str] = None
    ticket_type: Optional[str] = None
    status: Optional[str] = None
    updated_at: Optional[datetime] = None
    resolved_at: Optional[datetime] = None

    class Config:
        orm_mode = True
        from_attributes = True
