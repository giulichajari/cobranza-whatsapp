from datetime import datetime
from decimal import Decimal

from sqlalchemy import DateTime, ForeignKey, Integer, Numeric, String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.database.base import Base

class Pago(Base):
    __tablename__ = "pagos"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
    )

    cliente_id: Mapped[int] = mapped_column(
        ForeignKey("clientes.id"),
        nullable=False,
        index=True
    )

    importe: Mapped[Decimal] = mapped_column(
        Numeric(10, 2),
        nullable=False
    )

    fecha_pago: Mapped[datetime] = mapped_column(
        DateTime,
        nullable=False
    )

    estado: Mapped[str] = mapped_column(
        String(20),
        nullable=False
    )

    cliente = relationship(
        "Cliente",
        back_populates="pagos"
    )