"""Popula o banco com dados de exemplo."""

from backend.database.session import Base, engine, SessionLocal
from backend.schemas.usuario import UsuarioCreate
from backend.schemas.lead import LeadCreate
from backend.schemas.contato import ContatoCreate
from backend.services import auth_service, lead_service


def main():
    Base.metadata.create_all(bind=engine)
    with SessionLocal() as db:
        usuario = auth_service.obter_usuario_por_email(db, "demo@rotahunter.com")
        if not usuario:
            usuario = auth_service.criar_usuario(
                db, UsuarioCreate(nome="Demo Hunter", email="demo@rotahunter.com", senha="senha-demo")
            )
        lead = lead_service.criar_lead(
            db,
            LeadCreate(nome_empresa="Tech Brasil", setor="Tecnologia", regiao="SP", porte="Grande"),
            usuario.id,
        )
        lead_service.registrar_contato(
            db,
            lead.id,
            ContatoCreate(nome="Marina Compras", cargo="Head Compras", email="marina@techbr.com", whatsapp="5511988887777"),
        )
        print("Base populada com sucesso")


if __name__ == "__main__":
    main()
