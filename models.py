from pydantic import BaseModel

class Producto(BaseModel):
    nombre:str
    referencia:str
    precio_cop:float
    precio_usd:float
    estado:int
    