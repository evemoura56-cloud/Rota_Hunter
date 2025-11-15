"""Script para treinar o modelo comercial local."""

from backend.schemas.ia import TreinoLead, TreinoRequest
from backend.services.ia_service import ModeloIAService


def main():
    dataset = TreinoRequest(
        dados=[
            TreinoLead(
                setor="Tecnologia",
                porte="Grande",
                regiao="SP",
                interacoes=6,
                tempo_resposta_horas=4,
                status_pipeline="PROPOSTA",
                abertura_email=0.8,
                ganho=1,
            ),
            TreinoLead(
                setor="Servicos",
                porte="Medio",
                regiao="RJ",
                interacoes=2,
                tempo_resposta_horas=30,
                status_pipeline="PROSPECTADO",
                abertura_email=0.1,
                ganho=0,
            ),
        ]
    )
    ModeloIAService().treinar(dataset)
    print("Modelo treinado e salvo em disco")


if __name__ == "__main__":
    main()
