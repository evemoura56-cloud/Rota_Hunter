import urllib.parse


def gerar_link(telefone: str, mensagem: str) -> str:
    numero = telefone.replace("+", "")
    texto = urllib.parse.quote(mensagem)
    return f"https://wa.me/{numero}?text={texto}"
