from fastapi import FastAPI
from typing import List
from uuid import UUID, uuid4
from UserModel import Genero, Role, Usuario

app = FastAPI()

bd: List[Usuario] = [
    Usuario(
        id=uuid4(),
        nombre="Antonio",
        apellidos="Cruz",
        genero=Genero.masculino,
        roles=[Role.user]
    ),
    Usuario(
        id=uuid4(),
        nombre="Miguel",
        apellidos="Garcia",
        genero=Genero.masculino,
        roles=[Role.admin]
    ),
    Usuario(
        id=uuid4(),
        nombre="Rosario",
        apellidos="Tijeras",
        genero=Genero.masculino,
        roles=[Role.invitado]
    ),
]

@app.get("/")
async def root():
    """Endpoint raíz de prueba"""
    return{"saludo": "Hola buen día"}

@app.get("/api/v1/users")
async def get_users():
    """Lista de usuarios"""
    return bd

@app.post("/api/v1/users")
async def create_user(user: Usuario):
    bd.append(user)
    return user


@app.put("/api/v1/users/{user_id}", response_model=Usuario)
async def update_user(user_id: UUID, user_update: Usuario):
    for index, user  in enumerate(db):
        if user.id == user_id:
            user_update.id = user_id
            bd[index] = user_update
            return user_update
    raise HTTPException(status_code=404, detail="Usuario no encontrado")






@app.delete("/api/v1/users/{user_id}")
async def delete_user(user_id: UUID):
    for user in db [:]:
        if user.id == user_id:
            bd.remove(user)
            return {"mensaje": "El usuario se ha eliminado exitosamente"}
    raise HTTPException(status_code=404, detail="El usuario no se pudo encontrar")






@app.get("/")
def root():
    return {"saludo": "Hola buen día"}
@app.get("/api/v1/users")
async def get_users():
        return bd

