import uuid
from typing import Union, Dict, Any
from uuid import UUID

from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.database.models import User


# =================================================================================================================== #
# ------------------------------------------------------ USER ------------------------------------------------------- #
# =================================================================================================================== #

def create_user(db: Session, data: Dict[str, Any]) -> Union[User, None]:
    try:
        new_one = User(**data, id=uuid.uuid4())
        db.add(new_one)
        db.commit()
        db.refresh(new_one)
        return new_one
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE user: {str(e)}"
    finally:
        db.close()


def read_user(db: Session, user_id: UUID) -> Union[User, None]:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        return user
    except SQLAlchemyError as e:
        raise f"Error READ user: {str(e)}"
    finally:
        db.close()


def read_users(db: Session):
    users = db.query(User).all()
    return users


def update_user(db: Session, user_id: UUID, user_data: Dict[str, Any]) -> bool:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        for attr, value in user_data.items():
            setattr(user, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE user: {str(e)}"
    finally:
        db.close()


def delete_user(db: Session, user_id: UUID) -> bool:
    try:
        user = db.query(User).filter(User.id == user_id).first()
        if not user:
            raise ValueError("User not found")

        db.delete(user)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE user: {str(e)}"
    finally:
        db.close()
