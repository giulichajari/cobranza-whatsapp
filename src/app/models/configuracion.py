from decimal import Decimal

from sqlalchemy import Integer, Numeric, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.database.base import Base


class Configuracion(Base):
    __tablename__ = "configuracion"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id"),
        nullable=False,
        unique=True,   # 👈 clave: 1 config por cliente
        index=True
    )

    importe_mensual: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    dias_recordatorio: Mapped[int] = mapped_column(
        Integer,
        nullable=False,
        default=3
    )

    # relación opcional (recomendado)
    cliente = relationship(
        "Cliente",
        back_populates="configuracion"
    )