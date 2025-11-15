"""Fluxo simplificado usando Playwright (modo headless)."""

from typing import Any

try:
    from playwright.sync_api import sync_playwright
except Exception:  # noqa: BLE001
    sync_playwright = None  # Playwright opcional durante desenvolvimento


def executar_pre_cadastro(url: str) -> dict[str, Any]:
    """Retorna dados coletados durante preenchimento de fornecedores."""

    resultado = {
        "url_cadastro": url,
        "status_preenchimento": "PENDENTE",
        "possui_captcha": False,
        "exige_upload": False,
        "erros_detectados": None,
    }

    if not sync_playwright:
        return resultado

    with sync_playwright() as p:
        navegador = p.chromium.launch(headless=True)
        pagina = navegador.new_page()
        pagina.goto(url, wait_until="domcontentloaded")
        campos = pagina.query_selector_all("input")
        for campo in campos[:3]:
            campo.fill("Rota Hunter")
        resultado["status_preenchimento"] = "ENVIADO"
        if pagina.query_selector("text=CAPTCHA"):
            resultado["possui_captcha"] = True
        if pagina.query_selector("input[type=file]"):
            resultado["exige_upload"] = True
        navegador.close()
    return resultado
