from datetime import datetime, timedelta
from typing import Optional

from fastapi import HTTPException, status
from jose import jwt
from passlib.context import CryptContext
from sqlalchemy.orm import Session

from backend.models import Usuario
from backend.schemas.usuario import UsuarioCreate
from backend.src.common.config import get_settings

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
settings = get_settings()


def obter_usuario_por_email(db: Session, email: str) -> Optional[Usuario]:
    return db.query(Usuario).filter(Usuario.email == email).first()


def criar_usuario(db: Session, payload: UsuarioCreate) -> Usuario:
    if obter_usuario_por_email(db, payload.email):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Email ja cadastrado")
    usuario = Usuario(
        nome=payload.nome,
        email=payload.email,
        senha_hash=pwd_context.hash(payload.senha),
    )
    db.add(usuario)
    db.commit()
    db.refresh(usuario)
    return usuario


def autenticar_usuario(db: Session, email: str, senha: str) -> Usuario:
    usuario = obter_usuario_por_email(db, email)
    if not usuario or not pwd_context.verify(senha, usuario.senha_hash):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciais invalidas")
    return usuario


def criar_token(usuario: Usuario) -> str:
    expiracao = datetime.utcnow() + timedelta(hours=settings.jwt_exp_horas)
    payload = {"sub": str(usuario.id), "exp": expiracao}
    return jwt.encode(payload, settings.jwt_secret, algorithm=settings.jwt_algorithm)


def autenticar_token(token: str, db: Session) -> Usuario:
    try:
        payload = jwt.decode(token, settings.jwt_secret, algorithms=[settings.jwt_algorithm])
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido") from exc

    usuario_id = payload.get("sub")
    usuario = db.get(Usuario, int(usuario_id)) if usuario_id else None
    if not usuario:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Usuario nao encontrado")
    return usuario
