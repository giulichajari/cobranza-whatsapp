from decimal import Decimal

from sqlalchemy import Integer, Numeric
from sqlalchemy.orm import Mapped, mapped_column

from src.app.database.base import Base


class Configuracion(Base):
    __tablename__ = "configuracion"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True
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