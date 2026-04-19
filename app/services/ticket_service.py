from sqlalchemy.orm import Session
from app.models.tickets import Ticket
from datetime import datetime


def create_ticket(db: Session, ticket_data):
    new_ticket = Ticket(
        ticket_no=ticket_data.ticket_no,
        description=ticket_data.description,
        ticket_type=ticket_data.ticket_type,
        status=ticket_data.status,
        ticket_owner=ticket_data.ticket_owner,
        store_id=ticket_data.store_id,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(new_ticket)
    db.commit()
    db.refresh(new_ticket)
    return new_ticket


def get_all_tickets(db: Session):
    return db.query(Ticket).all()


def get_ticket_by_id(db: Session, ticket_id: int):
    return db.query(Ticket).filter(Ticket.id == ticket_id).first()


def update_ticket(db: Session, ticket_id: int, ticket_data):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        return None
    for key, value in ticket_data.dict(exclude_unset=True).items():
        setattr(ticket, key, value)
    if ticket.status.lower() == "closed" and not ticket.resolved_at:
        ticket.resolved_at = datetime.utcnow()
    ticket.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(ticket)
    return ticket


def delete_ticket(db: Session, ticket_id: int):
    ticket = db.query(Ticket).filter(Ticket.id == ticket_id).first()
    if not ticket:
        return None
    db.delete(ticket)
    db.commit()
    return ticket
