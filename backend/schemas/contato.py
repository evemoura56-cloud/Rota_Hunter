from pydantic import BaseModel, EmailStr
from typing import Optional


class ContatoCreate(BaseModel):
    nome: str
    cargo: Optional[str] = None
    email: Optional[EmailStr] = None
    whatsapp: Optional[str] = None


class ContatoRead(ContatoCreate):
    id: int

    class Config:
        from_attributes = True
