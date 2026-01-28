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
def root():
    return {"saludo": "Hola buen día"}
@app.get("/api/v1/users")
async def get_users():
        return bd

