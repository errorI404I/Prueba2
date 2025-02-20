from fastapi import FastAPI
from .routers import user, activity
from .database import engine, Base

# Crear las tablas en la base de datos
Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(user.router)
app.include_router(activity.router)

@app.get("/")
def read_root():
    return {"message": "Bienvenido al API del campus de entrenamiento de fútbol"}

@app.get("/api/users")
async def get_users():
    return [{"name": "User1"}, {"name": "User2"}] 