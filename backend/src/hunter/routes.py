from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.services import hunter_service
from backend.src.common.deps import get_db_session, get_usuario_atual


class DiscoverRequest(BaseModel):
    setor: str | None = None
    regiao: str | None = None
    palavras_chave: list[str] = Field(default_factory=list)


router = APIRouter(prefix="/hunter", tags=["Prospecao"])


@router.post("/discover")
def discover(
    payload: DiscoverRequest,
    db: Session = Depends(get_db_session),
    usuario=Depends(get_usuario_atual),
):
    return {
        "resultado": hunter_service.descobrir_empresas(db, payload.model_dump(), usuario.id),
        "mensagem": "Novos leads cadastrados",
    }
