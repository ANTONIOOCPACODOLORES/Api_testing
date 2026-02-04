from enum import Enum
from pydantic import BaseModel
from typing import List
from uuid import UUID

class Genero(str, Enum):
    masculino = "masculino"
    femenino = "femenino"
    otro = ""

class Role(str, Enum):
    admin = "admin"
    user = "user"
    invitado = "invitado"

class Usuario(BaseModel):
    id: UUID
    nombre: str
    apellidos: str
    genero: Genero
    roles: List[Role]
    
