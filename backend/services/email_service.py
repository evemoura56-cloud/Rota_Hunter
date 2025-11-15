import smtplib
from email.mime.text import MIMEText
from typing import Iterable

from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from backend.models import Lead, Contato, Interacao, TipoInteracao
from backend.src.common.config import get_settings

settings = get_settings()


class EmailLoteResultado:
    def __init__(self, enviados: int, ignorados: int) -> None:
        self.enviados = enviados
        self.ignorados = ignorados


class EmailService:
    def __init__(self, db: Session) -> None:
        self.db = db

    def _render_texto(self, corpo: str, contato: Contato, lead: Lead) -> str:
        mensagem = corpo.replace("{{nome_contato}}", contato.nome or "Contato")
        mensagem = mensagem.replace("{{nome_empresa}}", lead.nome_empresa)
        return mensagem

    def enviar_lote(self, ids_leads: Iterable[int], corpo: str, assunto: str) -> EmailLoteResultado:
        ids_unicos = list(dict.fromkeys(ids_leads))
        enviados = ignorados = 0
        servidor = None
        if settings.modo_envio_email == "smtp_real":
            servidor = smtplib.SMTP(settings.smtp_host, settings.smtp_porta)
            servidor.starttls()
            servidor.login(settings.smtp_usuario, settings.smtp_senha)
        try:
            for lead_id in ids_unicos:
                lead = self.db.get(Lead, lead_id)
                if not lead:
                    ignorados += 1
                    continue
                if not lead.contatos:
                    ignorados += 1
                    continue
                contato = lead.contatos[0]
                conteudo = self._render_texto(corpo, contato, lead)
                if settings.modo_envio_email == "smtp_real":
                    msg = MIMEText(conteudo, "plain", "utf-8")
                    msg["Subject"] = assunto
                    msg["From"] = settings.smtp_usuario
                    msg["To"] = contato.email or ""
                    if not contato.email:
                        ignorados += 1
                        continue
                    servidor.sendmail(settings.smtp_usuario, [contato.email], msg.as_string())
                enviados += 1
                interacao = Interacao(
                    lead=lead,
                    contato=contato,
                    tipo=TipoInteracao.EMAIL_AUTO,
                    conteudo=conteudo,
                )
                self.db.add(interacao)
            self.db.commit()
        finally:
            if servidor:
                servidor.quit()
        if enviados > settings.limite_email_diario:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Limite diario excedido")
        return EmailLoteResultado(enviados=enviados, ignorados=ignorados)
