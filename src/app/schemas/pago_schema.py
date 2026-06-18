from datetime import datetime
from decimal import Decimal

from pydantic import BaseModel


class PagoCreate(BaseModel):
    cliente_id: int
    importe: Decimal
    fecha_pago: datetime
    estado: str


class PagoUpdate(BaseModel):
    cliente_id: int
    importe: Decimal
    fecha_pago: datetime
    estado: str


class PagoResponse(BaseModel):
    id: int
    cliente_id: int
    importe: Decimal
    fecha_pago: datetime
    estado: str

    model_config = {
        "from_attributes": True
    }