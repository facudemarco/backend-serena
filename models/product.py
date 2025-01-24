from pydantic import BaseModel
from typing import Optional
from datetime import date

class Product(BaseModel):
    id: Optional[str] = None
    destino: str
    subtitulo: str
    date: date
    days: str
    nights: str
    regimen: str
    transporte: str
    periodo: str
    paquete: str
    descripcion: str
    moneda: str
    precio: str
    adicional: str
    image: str
    desde: bool
    hotel: str
    incluye: str
    observaciones: str
    itinerario: str
    itinerario2: str
    itinerario3: str
    itinerario4: str
    itinerario5: str
    itinerario6: str
    itinerario7: str
    itinerario8: str
    tarifas: str