from fastapi import APIRouter, Depends, HTTPException, status

from backend.schemas.ia import TreinoRequest, PredicaoRequest, PredicaoResponse
from backend.services.ia_service import ModeloIAService
from backend.src.common.deps import get_usuario_atual

router = APIRouter(prefix="/ia", tags=["Inteligencia"])


@router.post("/train")
def treinar(payload: TreinoRequest, usuario=Depends(get_usuario_atual)):
    servico = ModeloIAService()
    try:
        mensagem = servico.treinar(payload)
    except ValueError as exc:  # noqa: BLE001
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
    return {"mensagem": mensagem}


@router.post("/predict", response_model=PredicaoResponse)
def prever(payload: PredicaoRequest, usuario=Depends(get_usuario_atual)):
    servico = ModeloIAService()
    try:
        return servico.prever(payload)
    except ValueError as exc:  # noqa: BLE001
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(exc)) from exc
