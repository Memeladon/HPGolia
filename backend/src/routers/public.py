import mimetypes
import os

from fastapi import APIRouter, HTTPException
from starlette.responses import Response

router = APIRouter(tags=['storage'], prefix='/storage')
BASE_DIR = os.path.abspath('src/backend/public/storage')


@router.get('/{path}')
def get_one_profile_img(path: str):

    file_path = os.path.abspath(os.path.join(BASE_DIR, path))

    # Остался в BASE_DIR
    if not file_path.startswith(BASE_DIR):
        raise HTTPException(status_code=400, detail="Недопустимый путь")

    # Существует
    if not os.path.exists(file_path):
        raise HTTPException(status_code=404, detail="Файл не найден")

    # MIME-тип
    mime_type, _ = mimetypes.guess_type(file_path)
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Общий MIME-тип

    with open(file_path, 'rb') as file:
        content = file.read()

    return Response(content, media_type=mime_type)
