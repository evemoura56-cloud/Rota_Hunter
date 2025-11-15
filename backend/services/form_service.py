from backend.services import lead_service
from backend.src.forms.playwright_runner import executar_pre_cadastro


def automatizar_formulario(db, lead_id: int, url: str):
    resultado = executar_pre_cadastro(url)
    return lead_service.registrar_formulario(db, lead_id, resultado)
