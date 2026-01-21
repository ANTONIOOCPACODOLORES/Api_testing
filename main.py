from fastapi import FastAPI
from typing import List,Optional
from import UUID, uuid4
from userModel import Genero, Role,Usuario

app = FastAPI()
bd:List[Usuario]={
    Usuario(
        id=uuid4(),
        nombre="Antonio",
        apellidos="Cruz",
        genero=Genero.masculino,
        Roles=[Role.user]
    ),
     Usuario(
        id=uuid4(),
        nombre="Miguel
        apellidos="Garcia
        genero=Genero.masculino,
        Roles=[Role.admin],
    ),
      Usuario(
        id=uuid4(),
        nombre="Rosario
        apellidos="Tijeras
        genero=Genero.masculino,
        Roles=[Role.invitado]
    ),
}


@app.get("/")
def root():
    return {"saludo": "Hola buen día"}
@app.get("/api/v1/users")
async def get_users
