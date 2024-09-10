from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.orm import Session

from src.database.models import Cell


def read_cells(db: Session):
    try:
        cells = db.query(Cell).all()
        return cells
    except SQLAlchemyError as e:
        raise f"Error READ cells: {str(e)}"
    finally:
        db.close()
