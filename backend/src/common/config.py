from functools import lru_cache
from pydantic_settings import BaseSettings
from pydantic import AnyHttpUrl


class Settings(BaseSettings):
    ambiente: str = "desenvolvimento"
    app_nome: str = "Rota Hunter 1.0"
    database_url: str = "sqlite:///backend/database/rota_hunter.db"
    jwt_secret: str = "troque-me"
    jwt_algorithm: str = "HS256"
    jwt_exp_horas: int = 12
    limite_email_diario: int = 300
    smtp_host: str = "smtp.gmail.com"
    smtp_porta: int = 587
    smtp_usuario: str = ""
    smtp_senha: str = ""
    remetente_nome: str = "Equipe Rota Hunter"
    frontend_url: AnyHttpUrl | None = None
    caminho_modelo_ia: str = "./database/modelo_ia.pkl"
    modo_envio_email: str = "simulado"

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


@lru_cache(maxsize=1)
def get_settings() -> Settings:
    return Settings()
