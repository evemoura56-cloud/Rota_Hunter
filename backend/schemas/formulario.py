from pydantic import BaseModel


class FormularioRead(BaseModel):
    id: int
    url_cadastro: str | None = None
    status_preenchimento: str | None = None
    possui_captcha: bool
    exige_upload: bool
    erros_detectados: str | None = None

    class Config:
        from_attributes = True
