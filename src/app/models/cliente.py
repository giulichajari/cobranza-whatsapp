from datetime import date

from sqlalchemy import String, Integer, Date, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship

from src.app.database.base import Base


class Cliente(Base):
    __tablename__ = "clientes"

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        index=True
    )

    nombre: Mapped[str] = mapped_column(
        String(100),
        nullable=False
    )

    telefono: Mapped[str] = mapped_column(
        String(20),
        nullable=False,
        index=True
    )

    email: Mapped[str] = mapped_column(
        String(100),
        nullable=False,
        unique=True
    )

    fecha_vencimiento: Mapped[date] = mapped_column(
        Date,
        nullable=False
    )

    activo: Mapped[bool] = mapped_column(
        Boolean,
        default=True
    )

    pagos = relationship(
       "Pago",
       back_populates="cliente"
    )
    configuracion = relationship(
    "Configuracion",
    back_populates="cliente",
    uselist=False  # 👈 1 a 1
    )