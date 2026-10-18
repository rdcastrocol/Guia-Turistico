from fastapi import APIRouter, Depends, HTTPException, status

from sqlalchemy.orm import Session

from ..database import get_db

from ..exceptions import ID, NF

from ..repositories.note_repository import Repo

from ..schemas import NC, NR, NU

from ..services.deadline_manager import Std

from ..services.note_manager import Mgr

from ..services.note_service import Svc



router = APIRouter(
    prefix="/prompt",
    tags=["question"],
)
