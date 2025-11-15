from sqlalchemy import String, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from backend.database.session import Base


class FormularioFornecedor(Base):
    __tablename__ = "formularios_fornecedor"

    id: Mapped[int] = mapped_column(primary_key=True)
    lead_id: Mapped[int] = mapped_column(ForeignKey("leads.id", ondelete="CASCADE"))
    url_cadastro: Mapped[str | None] = mapped_column(String(255))
    status_preenchimento: Mapped[str | None] = mapped_column(String(80), default="PENDENTE")
    possui_captcha: Mapped[bool] = mapped_column(default=False)
    exige_upload: Mapped[bool] = mapped_column(default=False)
    erros_detectados: Mapped[str | None] = mapped_column(String(255))

    lead: Mapped["Lead"] = relationship(back_populates="formularios")
