from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.schemas.lead import LeadCreate, LeadUpdate, LeadRead, LeadStatusUpdate
from backend.schemas.contato import ContatoCreate, ContatoRead
from backend.schemas.interacao import InteracaoCreate, InteracaoRead
from backend.schemas.formulario import FormularioRead
from backend.services import lead_service
from backend.src.common.deps import get_db_session, get_usuario_atual

router = APIRouter(tags=["CRM"])


@router.post("/leads", response_model=LeadRead)
def criar_lead(payload: LeadCreate, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.criar_lead(db, payload, usuario.id)


@router.get("/leads", response_model=list[LeadRead])
def listar_leads(db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.listar_leads(db)


@router.get("/leads/{lead_id}", response_model=LeadRead)
def obter_lead(lead_id: int, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.obter_lead(db, lead_id)


@router.put("/leads/{lead_id}", response_model=LeadRead)
def atualizar_lead(lead_id: int, payload: LeadUpdate, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.atualizar_lead(db, lead_id, payload)


@router.put("/leads/{lead_id}/status", response_model=LeadRead)
def atualizar_status(lead_id: int, payload: LeadStatusUpdate, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.atualizar_status(db, lead_id, payload)


@router.post("/leads/{lead_id}/contacts", response_model=ContatoRead)
def criar_contato(lead_id: int, payload: ContatoCreate, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.registrar_contato(db, lead_id, payload)


@router.get("/leads/{lead_id}/contacts", response_model=list[ContatoRead])
def listar_contatos(lead_id: int, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    lead = lead_service.obter_lead(db, lead_id)
    return lead.contatos


@router.post("/leads/{lead_id}/interactions", response_model=InteracaoRead)
def criar_interacao(lead_id: int, payload: InteracaoCreate, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return lead_service.registrar_interacao(db, lead_id, payload)


@router.get("/leads/{lead_id}/interactions", response_model=list[InteracaoRead])
def listar_interacoes(lead_id: int, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    lead = lead_service.obter_lead(db, lead_id)
    return lead.interacoes


@router.get("/leads/{lead_id}/forms", response_model=list[FormularioRead])
def listar_formularios(lead_id: int, db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    lead = lead_service.obter_lead(db, lead_id)
    return lead.formularios


@router.get("/crm/dashboard")
def dashboard(db: Session = Depends(get_db_session), usuario=Depends(get_usuario_atual)):
    return {
        "status": lead_service.relatorio_funil(db),
        "setores": lead_service.leads_por_setor(db),
        "leads_quentes": lead_service.leads_quentes(db),
        "propostas_ativas": lead_service.propostas_ativas(db),
        "velocidade_funil": lead_service.velocidade_funil(db),
    }
