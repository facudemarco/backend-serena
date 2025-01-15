from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
    id: Optional[str] = None
    destino: str
    subtitulo: str
    date: date
    days: int
    nights: int
    regimen: str
    transporte: str
    periodo: str
    paquete: str
    descripcion: str
    moneda: str
    precio: int
    adicional: str
    img: str
    desde: bool
    hotel: str
    incluye: str
    observaciones: str
    itinerario: str
    tarifas: str