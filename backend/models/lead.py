from __future__ import annotations

from datetime import datetime
from enum import Enum
from sqlalchemy import String, Enum as SqlEnum, Float, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.session import Base


class StatusPipeline(str, Enum):
    PROSPECTADO = "PROSPECTADO"
    CONTATADO = "CONTATADO"
    RESPONDEU = "RESPONDEU"
    QUALIFICADO = "QUALIFICADO"
    PROPOSTA = "PROPOSTA"
    GANHO = "GANHO"
    PERDIDO = "PERDIDO"


class Lead(Base):
    __tablename__ = "leads"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nome_empresa: Mapped[str] = mapped_column(String(160))
    site_url: Mapped[str | None] = mapped_column(String(255))
    setor: Mapped[str | None] = mapped_column(String(120))
    porte: Mapped[str | None] = mapped_column(String(60))
    regiao: Mapped[str | None] = mapped_column(String(60))
    status_pipeline: Mapped[StatusPipeline] = mapped_column(SqlEnum(StatusPipeline), default=StatusPipeline.PROSPECTADO)
    p_win: Mapped[float] = mapped_column(Float, default=0.0)
    data_prospeccao: Mapped[datetime] = mapped_column(DateTime, default=datetime.utcnow)
    proprietario_id: Mapped[int | None] = mapped_column(ForeignKey("usuarios.id"), nullable=True)

    proprietario: Mapped["Usuario | None"] = relationship(back_populates="leads")
    contatos: Mapped[list["Contato"]] = relationship(back_populates="lead", cascade="all, delete-orphan")
    interacoes: Mapped[list["Interacao"]] = relationship(back_populates="lead", cascade="all, delete-orphan")
    formularios: Mapped[list["FormularioFornecedor"]] = relationship(back_populates="lead", cascade="all, delete-orphan")
