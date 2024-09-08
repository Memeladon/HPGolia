from uuid import UUID
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Union, Dict, Any

from src.database.models import SessionUser, User, Session as DBSession


# =================================================================================================================== #
# ------------------------------------------------------ SESSION ---------------------------------------------------- #
# =================================================================================================================== #

def create_session(db: Session, session_data: Dict[str, Any]) -> Union[DBSession, None]:
    try:
        required_fields = ['max_players', 'date_start', 'date_end']
        if not all(field in session_data for field in required_fields):
            raise ValueError("Missing required fields: max_players, date_start, date_end")

        new_session = DBSession(**session_data)
        db.add(new_session)
        db.commit()
        db.refresh(new_session)
        return new_session
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE session: {str(e)}"
    finally:
        db.close()


def read_session(db: Session, session_id: UUID) -> Union[DBSession, None]:
    try:
        session = db.query(DBSession).filter(DBSession.id == session_id).first()
        return session
    except SQLAlchemyError as e:
        raise f"Error READ session: {str(e)}"
    finally:
        db.close()


def update_session(db: Session, session_id: UUID, session_data: Dict[str, Any]) -> bool:
    try:
        session = db.query(DBSession).filter(DBSession.id == session_id).first()
        if not session:
            raise ValueError("Session not found")

        for attr, value in session_data.items():
            setattr(session, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE session: {str(e)}"
    finally:
        db.close()


def delete_session(db: Session, session_id: UUID) -> bool:
    try:
        session = db.query(DBSession).filter(DBSession.id == session_id).first()
        if not session:
            raise ValueError("Session not found")

        db.delete(session)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE session: {str(e)}"
    finally:
        db.close()


# =================================================================================================================== #
# -------------------------------------------------- SESSION USER --------------------------------------------------- #
# =================================================================================================================== #

def create_session_user(db: Session, session_user_data: Dict[str, Any]) -> Union[SessionUser, None]:
    try:
        required_fields = ['session', 'user', 'permission']
        if not all(field in session_user_data for field in required_fields):
            raise ValueError("Missing required fields: session, user, permission")

        new_session_user = SessionUser(**session_user_data)
        db.add(new_session_user)
        db.commit()
        db.refresh(new_session_user)
        return new_session_user
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE session_user: {str(e)}"
    finally:
        db.close()


def read_session_user(db: Session, session_user_id: int) -> Union[SessionUser, None]:
    try:
        session_user = db.query(SessionUser).filter(SessionUser.id == session_user_id).first()
        return session_user
    except SQLAlchemyError as e:
        raise f"Error READ session_user: {str(e)}"
    finally:
        db.close()


def update_session_user(db: Session, session_user_id: int, session_user_data: Dict[str, Any]) -> bool:
    try:
        session_user = db.query(SessionUser).filter(SessionUser.id == session_user_id).first()
        if not session_user:
            raise ValueError("Session_user not found")

        for attr, value in session_user_data.items():
            setattr(session_user, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE session_user: {str(e)}"
    finally:
        db.close()


def delete_session_user(db: Session, session_user_id: int) -> bool:
    try:
        session_user = db.query(SessionUser).filter(SessionUser.id == session_user_id).first()
        if not session_user:
            raise ValueError("Session_user not found")

        db.delete(session_user)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE session_user: {str(e)}"
    finally:
        db.close()


# =================================================================================================================== #
# ------------------------------------------------------ USER ------------------------------------------------------- #
# =================================================================================================================== #

def create_user(db: Session, user_data: Dict[str, Any]) -> Union[User, None]:
    try:
        required_fields = ['username', 'password', 'role', 'is_active']
        if not all(field in user_data for field in required_fields):
            raise ValueError("Missing required fields: username, password, role, is_active")

        new_user = User(**user_data)
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        return new_user
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
