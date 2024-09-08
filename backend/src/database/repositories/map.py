# ============================================================================================================ #
# -------------------------------------------------- FIELD --------------------------------------------------- #
# ============================================================================================================ #
from sqlalchemy.orm import Session

from backend.src.database.models import Field


def create_fields(fields_data: list, db: Session):
    db.bulk_insert_mappings(Field, fields_data)
    db.commit()


def get_all_fields(db: Session):
    return db.query(Field).all()


