from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.usuario import UsuarioCreate, UsuarioRead
from backend.schemas.auth import LoginRequest, TokenResponse
from backend.services import auth_service
from backend.src.common.deps import get_db_session, get_usuario_atual

router = APIRouter(prefix="/auth", tags=["Autenticacao"])


@router.post("/register", response_model=UsuarioRead)
def registrar(payload: UsuarioCreate, db: Session = Depends(get_db_session)):
    return auth_service.criar_usuario(db, payload)


@router.post("/login", response_model=TokenResponse)
def login(payload: LoginRequest, db: Session = Depends(get_db_session)):
    usuario = auth_service.autenticar_usuario(db, payload.email, payload.senha)
    token = auth_service.criar_token(usuario)
    return TokenResponse(access_token=token)


@router.get("/me", response_model=UsuarioRead)
def me(usuario=Depends(get_usuario_atual)):
    return usuario
