from pydantic import BaseModel, Field
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

from backend.services.email_service import EmailService
from backend.src.common.config import get_settings
from backend.src.common.deps import get_db_session, get_usuario_atual

settings = get_settings()


class EmailBatchRequest(BaseModel):
    lead_ids: list[int] = Field(default_factory=list)
    assunto: str
    corpo: str


router = APIRouter(prefix="/engagement", tags=["Engajamento"])


@router.post("/email-batch")
def enviar_lote(payload: EmailBatchRequest, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    if len(payload.lead_ids) > settings.limite_email_diario:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Quantidade acima do permitido")
    resultado = EmailService(db).enviar_lote(payload.lead_ids, payload.corpo, payload.assunto)
    return {"enviados": resultado.enviados, "ignorados": resultado.ignorados}
