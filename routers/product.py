from fastapi import APIRouter, HTTPException
from models.product import Product
from Database.dbGetConnection import getConnection
from Database.testConnection import get_connection
import uuid

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

def getProduct(id: str):
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
@router.post('/products/create_product')

def createProduct(product: Product):

    connection = getConnection()

    generated_id = str(uuid.uuid4())

    if connection is None:
        raise HTTPException(detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO `Products`(`ID`, `destino`, `subtitulo`, `date`, `days`, `nights`, `regimen`, `transporte`, `periodo`, `paquete`, `descripcion`, `moneda`, `precio`, `adicional`, `image`, `desde`, `hotel`, `incluye`, `observaciones`, `itinerario`, `tarifas`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)", (generated_id, product.destino, product.subtitulo, product.date, product.days, product.nights, product.regimen, product.transporte, product.periodo, product.paquete, product.descripcion, product.moneda, product.precio, product.adicional, product.image, product.desde, product.hotel, product.incluye, product.observaciones, product.itinerario, product.tarifas))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product created successfully, ID: " + generated_id}

# Modificar producto
@router.put('/products/{id}')

def modProduct(id: str, product: Product):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("UPDATE `Products` SET destino = %s, subtitulo = %s, date = %s, days = %s, nights = %s, regimen = %s, transporte = %s, periodo = %s, paquete = %s, descripcion = %s, moneda = %s, precio = %s, adicional = %s, image = %s, desde = %s, hotel = %s, incluye = %s, observaciones = %s, itinerario = %s, tarifas = %s WHERE id = %s", (product.destino, product.subtitulo, product.date, product.days, product.nights, product.regimen, product.transporte, product.periodo, product.paquete, product.descripcion, product.moneda, product.precio, product.adicional, product.image, product.desde, product.hotel, product.incluye, product.observaciones, product.itinerario, product.tarifas, id))
    connection.commit()

    cursor.close()

    connection.close()

    return {"message": "Product updated successfully"}

# Eliminar producto
@router.delete('/products/{id}')

def delProducts(id: str):
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor()

    cursor.execute("DELETE FROM `Products` WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Product deleted successfully"}