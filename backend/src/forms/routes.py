from pydantic import BaseModel
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.services import form_service
from backend.src.common.deps import get_db_session, get_usuario_atual

router = APIRouter(prefix="/forms", tags=["Formularios"])


class FormRequest(BaseModel):
    lead_id: int
    url_cadastro: str


@router.post("/auto-fill")
def auto_fill(payload: FormRequest, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    resultado = form_service.automatizar_formulario(db, payload.lead_id, payload.url_cadastro)
    return resultado
