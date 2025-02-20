from fastapi import APIRouter, Depends
from ..schemas.user import User, UserCreate
from ..dependencies import get_current_user

router = APIRouter()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate):
    # Lógica para crear un nuevo usuario
    pass

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, current_user: User = Depends(get_current_user)):
    # Lógica para obtener un usuario por ID
    pass 