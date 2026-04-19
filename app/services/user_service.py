from sqlalchemy.orm import Session
from app.models.users import User
from datetime import datetime
from app.schemas.users import UserCreate, UserBase
from app.core.security import hash_password


def get_all_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def create_user(db: Session, user: UserCreate):
    db_user = User(
        username=user.username,
        hashed_password=hash_password(user.password),
        email=user.email,
        is_admin=user.is_admin,
        phone=user.phone,
        full_name=user.full_name,
        employee_no=user.employee_no,
        department=user.department,
        city=user.city,
        store_id=user.store_id,
        is_active=user.is_active,
        created_at=datetime.utcnow(),
        updated_at=datetime.utcnow(),
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user


def update_user(db: Session, user_id: int, user: UserBase):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    for key, value in user.dict(exclude_unset=True).items():
        setattr(db_user, key, value)
    db_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if not db_user:
        return None
    is_active = 0
    setattr(db_user, "is_active", is_active)
    db_user.updated_at = datetime.utcnow()
    db.commit()
    db.refresh(db_user)
    return db_user
