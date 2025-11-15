from random import randint
from typing import Any

from sqlalchemy.orm import Session

from backend.schemas.lead import LeadCreate
from backend.schemas.contato import ContatoCreate
from backend.services import lead_service

setores_exemplo = [
    "Tecnologia",
    "Varejo",
    "Servicos",
    "Industria",
]

cargos = [
    ("Diretora de Compras", "compras@empresa.com"),
    ("Head de Operacoes", "operacoes@empresa.com"),
    ("Gerente Comercial", "comercial@empresa.com"),
]


def descobrir_empresas(db: Session, filtro: dict[str, Any], usuario_id: int | None) -> list[dict[str, Any]]:
    setor = filtro.get("setor") or setores_exemplo[randint(0, len(setores_exemplo) - 1)]
    regiao = filtro.get("regiao") or "Brasil"
    palavras = filtro.get("palavras_chave", [])

    resultados: list[dict[str, Any]] = []
    for i in range(3):
        empresa = {
            "nome_empresa": f"{setor} Insights {i+1}",
            "site_url": f"https://{setor.lower()}-{i+1}.com",
            "setor": setor,
            "regiao": regiao,
            "palavras": palavras,
        }
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
        decisor = cargos[randint(0, len(cargos) - 1)]
        contato = lead_service.registrar_contato(
            db, lead.id, ContatoCreate(nome="Decisor", cargo=decisor[0], email=decisor[1], whatsapp="+5511999999999")
        )
        resultados.append({"lead_id": lead.id, "contato_id": contato.id})
    return resultados
