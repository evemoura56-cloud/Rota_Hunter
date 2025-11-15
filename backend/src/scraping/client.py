"""Cliente ficticio de scraping para centralizar buscas locais."""

from typing import Iterable


def buscar_empresas(setor: str | None, regiao: str | None, palavras: Iterable[str]):
    yield {
        "nome": f"{setor or 'Negocio'} Especialista",
        "site": "https://exemplo-interno.com",
        "setor": setor or "Geral",
        "regiao": regiao or "Brasil",
    }
