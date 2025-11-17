from collections import defaultdict
from datetime import datetime, date
from typing import Sequence

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.models import Lead, StatusPipeline, Contato, Interacao, TipoInteracao, FormularioFornecedor
from backend.schemas.lead import LeadCreate, LeadUpdate, LeadStatusUpdate
from backend.schemas.contato import ContatoCreate
from backend.schemas.interacao import InteracaoCreate

ORDEM_PIPELINE = [
    StatusPipeline.PROSPECTADO,
    StatusPipeline.CONTATADO,
    StatusPipeline.RESPONDEU,
    StatusPipeline.QUALIFICADO,
    StatusPipeline.PROPOSTA,
    StatusPipeline.GANHO,
    StatusPipeline.PERDIDO,
]


class EmailControle:
    """Controle simples de envios diarios."""

    def __init__(self) -> None:
        self.reset_token = date.today()
        self.total = 0

    def contabilizar(self, quantidade: int) -> None:
        hoje = date.today()
        if hoje != self.reset_token:
            self.reset_token = hoje
            self.total = 0
        self.total += quantidade


controle_email = EmailControle()


def criar_lead(db: Session, payload: LeadCreate, usuario_id: int | None = None) -> Lead:
    lead = Lead(**payload.model_dump(), proprietario_id=usuario_id)
    db.add(lead)
    db.commit()
    db.refresh(lead)
    return lead


def listar_leads(db: Session) -> Sequence[Lead]:
    return db.query(Lead).order_by(Lead.data_prospeccao.desc()).all()


def obter_lead(db: Session, lead_id: int) -> Lead:
    lead = db.get(Lead, lead_id)
    if not lead:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Lead nao encontrado")
    return lead


def atualizar_lead(db: Session, lead_id: int, payload: LeadUpdate) -> Lead:
    lead = obter_lead(db, lead_id)
    for campo, valor in payload.model_dump(exclude_unset=True).items():
        setattr(lead, campo, valor)
    db.commit()
    db.refresh(lead)
    return lead


def atualizar_status(db: Session, lead_id: int, payload: LeadStatusUpdate) -> Lead:
    lead = obter_lead(db, lead_id)
    origem_idx = ORDEM_PIPELINE.index(lead.status_pipeline)
    destino_idx = ORDEM_PIPELINE.index(payload.status_pipeline)
    if destino_idx - origem_idx > 1:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Nao e permitido pular etapas do pipeline")
    lead.status_pipeline = payload.status_pipeline
    db.commit()
    db.refresh(lead)
    return lead


def registrar_contato(db: Session, lead_id: int, payload: ContatoCreate) -> Contato:
    lead = obter_lead(db, lead_id)
    contato = Contato(**payload.model_dump(), lead=lead)
    db.add(contato)
    db.commit()
    db.refresh(contato)
    return contato


def registrar_interacao(db: Session, lead_id: int, payload: InteracaoCreate) -> Interacao:
    lead = obter_lead(db, lead_id)
    if payload.contato_id:
        contato = db.query(Contato).filter_by(id=payload.contato_id, lead_id=lead.id).first()
        if not contato:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contato invalido para o lead")
    interacao = Interacao(**payload.model_dump(), lead=lead)
    db.add(interacao)
    db.commit()
    db.refresh(interacao)
    return interacao


def registrar_formulario(db: Session, lead_id: int, resultado: dict) -> FormularioFornecedor:
    lead = obter_lead(db, lead_id)
    formulario = FormularioFornecedor(lead=lead, **resultado)
    db.add(formulario)
    db.commit()
    db.refresh(formulario)
    return formulario


def relatorio_funil(db: Session) -> dict[str, int]:
    contagem = defaultdict(int)
    for status_item in db.query(Lead.status_pipeline).all():
        contagem[status_item[0].value] += 1
    return contagem


def leads_por_setor(db: Session) -> dict[str, int]:
    contagem = defaultdict(int)
    for setor, _ in db.query(Lead.setor, Lead.id).filter(Lead.setor.isnot(None)).all():
        contagem[setor] += 1
    return contagem


def leads_quentes(db: Session) -> int:
    return db.query(Lead).filter(Lead.p_win >= 0.7).count()


def propostas_ativas(db: Session) -> int:
    return db.query(Lead).filter(Lead.status_pipeline == StatusPipeline.PROPOSTA).count()


def velocidade_funil(db: Session) -> float:
    primeiros = db.query(Lead).filter(Lead.status_pipeline == StatusPipeline.GANHO).all()
    if not primeiros:
        return 0.0
    tempos = [
        (lead.data_prospeccao - datetime.utcnow()).days * -1 or 1
        for lead in primeiros
    ]
    return sum(tempos) / len(tempos)


def get_lead_by_url(db: Session, site_url: str) -> Lead | None:
    return db.query(Lead).filter(Lead.site_url == site_url).first()
