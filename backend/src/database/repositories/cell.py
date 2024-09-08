import json

from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError
from typing import Union, Dict, Any, List

from src.database.models import Cell


# На случай, если нужно будет парсить условия
def parse_conditions(conditions_str: str) -> Dict[str, Any]:
    try:
        return json.loads(conditions_str)
    except json.JSONDecodeError:
        return {}


# =================================================================================================================== #
# ------------------------------------------------------- CELL ------------------------------------------------------ #
# =================================================================================================================== #

def create_cell(db: Session, cell_data: Dict[str, Any]) -> Union[Cell, None]:
    try:
        required_fields = ['position', 'title', 'type', 'main_conditions', 'genre_conditions']
        if not all(field in cell_data for field in required_fields):
            raise ValueError("Missing required fields: position, title, type, main_conditions, genre_conditions")

        new_cell = Cell(**cell_data)
        db.add(new_cell)
        db.commit()
        db.refresh(new_cell)
        return new_cell
    except SQLAlchemyError as e:
        db.rollback()
        raise f"Error CREATE cell: {str(e)}"
    finally:
        db.close()


def create_cells(db: Session, cells_data: List[Dict[str, Any]]) -> Union[List[Cell], None]:
    try:
        required_fields = ['position', 'title', 'type', 'main_conditions', 'genre_conditions']
        if not all(all(field in cell for cell in cells_data) for field in required_fields):
            raise ValueError("Missing required fields: position, title, type, main_conditions, genre_conditions")

        cells = [Cell(**cell_data) for cell_data in cells_data]

        db.add_all(cells)
        db.flush()
        db.commit()

        return None
    except SQLAlchemyError as e:
        print(f"Error MANY CREATE cells: {str(e)}")
        db.rollback()
        return None
    finally:
        db.close()


def read_cell(db: Session, cell_id: int) -> Union[Cell, None]:
    try:
        cell = db.query(Cell).filter(Cell.id == cell_id).first()
        return cell
    except SQLAlchemyError as e:
        raise f"Error READ cell: {str(e)}"
    finally:
        db.close()


def update_cell(db: Session, cell_id: int, cell_data: Dict[str, Any]) -> bool:
    try:
        cell = db.query(Cell).filter(Cell.id == cell_id).first()
        if not cell:
            raise ValueError("Cell not found")

        for attr, value in cell_data.items():
            setattr(cell, attr, value)

        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error UPDATE cell: {str(e)}"
    finally:
        db.close()


def delete_cell(db: Session, cell_id: int) -> bool:
    try:
        cell = db.query(Cell).filter(Cell.id == cell_id).first()
        if not cell:
            raise ValueError("Cell not found")

        db.delete(cell)
        db.commit()
        return True
    except (SQLAlchemyError, ValueError) as e:
        db.rollback()
        raise f"Error DELETE cell: {str(e)}"
    finally:
        db.close()
