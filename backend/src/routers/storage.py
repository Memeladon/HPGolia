import mimetypes
import os
from pathlib import Path

from fastapi import APIRouter, HTTPException
from starlette.responses import Response

router = APIRouter(tags=['storage'], prefix='/storage')

# Базовая директория для хранения файлов
BASE_DIR = Path('public/storage/')
ALLOWED_FOLDERS = {'players', 'cells', 'items'}


@router.get('/{folder}/{filename}')
def get_file(folder: str, filename: str):
    # Проверяем, что папка в области разрешенных
    if folder not in ALLOWED_FOLDERS:
        raise HTTPException(status_code=400, detail="Invalid folder path")

    file_path = BASE_DIR / folder / filename

    # Файл находится в пределах BASE_DIR и существует
    if not file_path.is_file() or BASE_DIR not in file_path.parents:
        raise HTTPException(status_code=404, detail=f"File not found")

    # Определяем MIME-тип файла
    mime_type, _ = mimetypes.guess_type(str(file_path))
    if mime_type is None:
        mime_type = 'application/octet-stream'  # Общий MIME-тип

    with open(file_path, 'rb') as file:
        content = file.read()

    return Response(content, media_type=mime_type)
