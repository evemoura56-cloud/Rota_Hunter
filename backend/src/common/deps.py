from fastapi import Depends, Header, HTTPException, status
from sqlalchemy.orm import Session

from backend.database.session import get_db
from backend.services import auth_service


def get_db_session() -> Session:
    yield from get_db()


def get_usuario_atual(
    db: Session = Depends(get_db_session),
    authorization: str | None = Header(default=None, alias="Authorization"),
):
    if not authorization:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token ausente")
    scheme, _, token = authorization.partition(" ")
    if scheme.lower() != "bearer" or not token:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token invalido")
    return auth_service.autenticar_token(token, db)
