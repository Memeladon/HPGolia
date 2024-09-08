from fastapi import APIRouter

router = APIRouter(tags=['users'], prefix='/users')


@router.get('/')
def get_all_user():
    return []


@router.get('/{id}')
def get_one_user(id):
    return {}


@router.put('/{id}')
def update_one_user(id):
    return {}


@router.delete('/{id}')
def delete_one_user(id):
    return {"msg": "ok"}
