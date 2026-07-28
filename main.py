from fastapi import FastAPI
from database import crear_tabla, get_connection
from models import Producto

app = FastAPI()

crear_tabla()

@app.get("/producto")
def crear_producto(producto:Producto):
    
    conn = get_connection()
    
    conn.execute("INSERT INTO productos" \
        "(nombre, descripcion, precio_cop, precio_usd, estado) VALUES(?,?,?,?,?)",(producto.nombre, producto.descripcion, producto.precio_cop, producto.precio_usd, producto.estado))
    
    conn.commit()
    conn.close()
    
    return{"mensaje":"Producto creado"}

@app.get("/lista_productos")
def listar():
    
    conn = get_connection()
    
    productos = conn.execute(
        "SELECT * FROM productos"
    ).fetchall()
    
    conn.close()
    return[dict(x) for x in productos]