from datetime import datetime
from pydantic import BaseModel, EmailStr, Field


class UsuarioCreate(BaseModel):
    nome: str = Field(..., min_length=3)
    email: EmailStr
    senha: str = Field(..., min_length=8)


class UsuarioRead(BaseModel):
    id: int
    nome: str
    email: EmailStr
    criado_em: datetime

    class Config:
        from_attributes = True
