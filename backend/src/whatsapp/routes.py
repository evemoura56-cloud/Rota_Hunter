from pydantic import BaseModel
from fastapi import APIRouter, Depends

from backend.services.whatsapp_service import gerar_link
from backend.src.common.deps import get_usuario_atual

router = APIRouter(prefix="/whatsapp", tags=["WhatsApp"])


class WhatsRequest(BaseModel):
    telefone: str
    mensagem: str


@router.post("/link")
def criar_link(payload: WhatsRequest, usuario=Depends(get_usuario_atual)):
    return {"link": gerar_link(payload.telefone, payload.mensagem)}
