from datetime import datetime
from typing import Optional
from pydantic import BaseModel

from backend.models.interacao import TipoInteracao


class InteracaoCreate(BaseModel):
    tipo: TipoInteracao
    contato_id: Optional[int] = None
    conteudo: Optional[str] = None


class InteracaoRead(InteracaoCreate):
    id: int
    data: datetime

    class Config:
        from_attributes = True
