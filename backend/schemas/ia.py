from pydantic import BaseModel, Field
from typing import Literal


class TreinoLead(BaseModel):
    setor: str
    porte: str
    regiao: str
    interacoes: int = Field(ge=0)
    tempo_resposta_horas: float = Field(ge=0)
    status_pipeline: str
    abertura_email: float = Field(ge=0, le=1)
    ganho: int = Field(ge=0, le=1)


class TreinoRequest(BaseModel):
    dados: list[TreinoLead]


class PredicaoRequest(BaseModel):
    setor: str
    porte: str
    regiao: str
    interacoes: int = Field(ge=0)
    tempo_resposta_horas: float = Field(ge=0)
    status_pipeline: str
    abertura_email: float = Field(ge=0, le=1)


class PredicaoResponse(BaseModel):
    p_win: float
    motivo_principal: str
    fatores: list[str]
