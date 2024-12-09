from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    id: str
    destino: str
    subtitulo: str
    descripcion: str
    fecha_de_salida: str
    dias: int
    noches: int
    regimen: str
    transporte: str
    periodo: str
    tipo_de_paquete: str
    moneda: str
    precio: int
    precio_adicional: str
    hotel: str
    image_url: str