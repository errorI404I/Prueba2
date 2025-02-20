from fastapi import APIRouter, Depends
from ..schemas.activity import Activity
from ..dependencies import get_current_user

router = APIRouter()

@router.post("/activities/", response_model=Activity)
def create_activity(activity: Activity):
    # Lógica para crear una nueva actividad
    pass

@router.get("/activities/")
def read_activities():
    # Lógica para obtener todas las actividades
    pass 