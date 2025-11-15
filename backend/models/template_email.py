from sqlalchemy import String, Text
from sqlalchemy.orm import Mapped, mapped_column

from backend.database.session import Base


class TemplateEmail(Base):
    __tablename__ = "templates_email"

    id: Mapped[int] = mapped_column(primary_key=True)
    nome_template: Mapped[str] = mapped_column(String(100), unique=True)
    assunto: Mapped[str] = mapped_column(String(150))
    corpo: Mapped[str] = mapped_column(Text)
