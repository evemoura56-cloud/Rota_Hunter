from datetime import datetime
from enum import Enum
from sqlalchemy import String, Text, DateTime, ForeignKey, Enum as SqlEnum
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.session import Base


class TipoInteracao(str, Enum):
    EMAIL_AUTO = "EMAIL_AUTO"
    WHATSAPP_MANUAL = "WHATSAPP_MANUAL"
    FOLLOW_UP = "FOLLOW_UP"
    NOTA = "NOTA"


class Interacao(Base):
    __tablename__ = "interacoes"

    id: Mapped[int] = mapped_column(primary_key=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"))
    contato_id: Mapped[int | None] = mapped_column(ForeignKey("contatos.id", ondelete="SET NULL"), nullable=True)
    tipo: Mapped[TipoInteracao] = mapped_column(SqlEnum(TipoInteracao))
    data: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    conteudo: Mapped[str | None] = mapped_column(Text)

    lead: Mapped["Lead"] = relationship(back_populates="interacoes")
    contato: Mapped["Contato | None"] = relationship(back_populates="interacoes")
