from decimal import Decimal
from pydantic import BaseModel


class ConfiguracionCreate(BaseModel):
    cliente_id: int
    importe_mensual: Decimal
    dias_recordatorio: int = 3


class ConfiguracionUpdate(BaseModel):
    importe_mensual: Decimal
    dias_recordatorio: int


class ConfiguracionResponse(BaseModel):
    id: int
    cliente_id: int
    importe_mensual: Decimal
    dias_recordatorio: int

    model_config = {
        "from_attributes": True
    }