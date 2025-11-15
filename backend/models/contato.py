from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.session import Base


class Contato(Base):
    __tablename__ = "contatos"

    id: Mapped[int] = mapped_column(primary_key=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"))
    nome: Mapped[str] = mapped_column(String(120))
    cargo: Mapped[str | None] = mapped_column(String(120))
    email: Mapped[str | None] = mapped_column(String(160))
    whatsapp: Mapped[str | None] = mapped_column(String(40))

    lead: Mapped["Lead"] = relationship(back_populates="contatos")
    interacoes: Mapped[list["Interacao"]] = relationship(back_populates="contato")
