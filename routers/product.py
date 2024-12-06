from fastapi import APIRouter, HTTPException
from models.product import Product
from Database.dbGetConnection import getConnection
from Database.testConnection import get_connection

router = APIRouter()

@router.get('/teste-database')

def testeDatabase():
    connection = get_connection()
    return {"message": "Database connection successful"}

# Get all products

@router.get('/products')

def getProducts():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Products`")

    products = cursor.fetchall()
    cursor.close()

    connection.close()
    return products
    
# Filter products by id

@router.get('/products/{id}')

def getProduct(id: int):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM `Products` WHERE id = %s", (id,))

    product = cursor.fetchone()
    cursor.close()

    connection.close()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

# Crear producto
@router.post('/products')

def createProduct(product: Product):

    connection = getConnection()

    if connection is None:
        raise HTTPException(detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `Products` (destino, subtitulo, descripcion, fecha-de-salida, dias, noches, regimen, transporte, periodo, tipo-de-paquete, moneda, precio, precio-adicional, hotel, image_url) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)",
                   (product.destino, product.subtitulo, product.descripcion, product.fecha_de_salida, product.dias, product.noches, product.regimen, product.transporte, product.periodo, product.tipo_de_paquete, product.moneda, product.precio, product.precio_adicional, product.hotel, product.image_url))

    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product created successfully"}

# Modificar producto
@router.put('/products/{id}')

def modProduct(id: int, product: Product):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `Products` SET destino = %s, subtitulo = %s, descripcion = %s, fecha-de-salida = %s, dias = %s, noches = %s, regimen = %s, transporte = %s, periodo = %s, tipo-de-paquete = %s, moneda = %s, precio = %s, precio-adicional = %s, hotel = %s, image_url = %s WHERE id = %s",
                   (product.destino, product.subtitulo, product.descripcion, product.fecha_de_salida, product.dias, product.noches, product.regimen, product.transporte, product.periodo, product.tipo_de_paquete, product.moneda, product.precio, product.precio_adicional, product.hotel, product.image_url, id))

    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product updated successfully"}

# Eliminar producto
@router.delete('/products/{id}')

def delProducts(id: int):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `Products` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Product deleted successfully"}