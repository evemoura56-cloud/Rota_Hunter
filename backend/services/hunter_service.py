import json
from typing import Any
from sqlalchemy.orm import Session

from backend.schemas.lead import LeadCreate
from backend.schemas.contato import ContatoCreate
from backend.services import lead_service

cargos = [
    ("Diretora de Compras", "compras@empresa.com"),
    ("Head de Operacoes", "operacoes@empresa.com"),
    ("Gerente Comercial", "comercial@empresa.com"),
]

def carregar_empresas_mock():
    with open("backend/services/empresas_mock.json", "r", encoding="utf-8") as f:
        return json.load(f)

def descobrir_empresas(db: Session, filtro: dict[str, Any], usuario_id: int | None) -> list[dict[str, Any]]:
    setor = filtro.get("setor")
    regiao = filtro.get("regiao")

    empresas = carregar_empresas_mock()

    empresas_filtradas = []
    for empresa in empresas:
        if (not setor or empresa["setor"].lower() == setor.lower()) and \
           (not regiao or empresa["regiao"].lower() == regiao.lower()):
            empresas_filtradas.append(empresa)

    resultados = []
    for empresa in empresas_filtradas:
        if lead_service.get_lead_by_url(db, empresa["site_url"]):
            continue

        lead = lead_service.criar_lead(
            db,
            LeadCreate(
                nome_empresa=empresa["nome_empresa"],
                site_url=empresa["site_url"],
                setor=empresa["setor"],
                regiao=empresa["regiao"],
                porte="Medio",
            ),
            usuario_id,
        )

        decisor = cargos[len(resultados) % len(cargos)]
        contato = lead_service.registrar_contato(
            db, lead.id, ContatoCreate(nome="Decisor", cargo=decisor[0], email=decisor[1], whatsapp="+5511999999999")
        )
        resultados.append({"lead_id": lead.id, "contato_id": contato.id})

    return resultados
