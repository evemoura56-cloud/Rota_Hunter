from datetime import datetime
from typing import Optional
from pydantic import BaseModel, Field

from backend.models.lead import StatusPipeline
from backend.schemas.contato import ContatoRead
from backend.schemas.interacao import InteracaoRead
from backend.schemas.formulario import FormularioRead


class LeadBase(BaseModel):
    nome_empresa: str = Field(..., min_length=2)
    site_url: Optional[str] = None
    setor: Optional[str] = None
    porte: Optional[str] = None
    regiao: Optional[str] = None


class LeadCreate(LeadBase):
    pass


class LeadUpdate(BaseModel):
    site_url: Optional[str] = None
    setor: Optional[str] = None
    porte: Optional[str] = None
    regiao: Optional[str] = None
    p_win: Optional[float] = Field(None, ge=0, le=1)


class LeadStatusUpdate(BaseModel):
    status_pipeline: StatusPipeline


class LeadRead(LeadBase):
    id: int
    status_pipeline: StatusPipeline
    p_win: float
    data_prospeccao: datetime
    contatos: list[ContatoRead] = []
    interacoes: list[InteracaoRead] = []
    formularios: list[FormularioRead] = []

    class Config:
        from_attributes = True
