from fastapi import APIRouter, HTTPException
from models.product import Product
from Database.dbGetConnection import getConnection

router = APIRouter()

# Get all products

@router.get('/products')

def getProducts():
    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products")

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

    cursor.execute("SELECT * FROM products WHERE id = %s", (id,))

    product = cursor.fetchone()
    cursor.close()

    connection.close()

    if product is None:
        raise HTTPException(status_code=404, detail="Product not found.")
    return product

# Filtrar productos por stock
@router.get('/products/')

def getProductsByStock(stock: int):

    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")

    cursor = connection.cursor(dictionary=True)

    cursor.execute("SELECT * FROM products WHERE stock = %s", (stock,))

    products = cursor.fetchall()

    cursor.close()
    connection.close()

    return products

# Crear producto
@router.post('/products')

def createProduct(product: Product):

    connection = getConnection()

    if connection is None:
        raise HTTPException(status_code=500, detail="Connection to the database failed.")
    cursor = connection.cursor()

    cursor.execute("INSERT INTO products (name, price, stock) VALUES (%s, %s, %s)",
                   (product.name, product.price, product.stock))

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

    cursor.execute("UPDATE products SET name = %s, price = %s, stock = %s WHERE id = %s",
                   (product.name, product.price, product.stock, id))

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

    cursor.execute("DELETE FROM products WHERE id = %s", (id,))

    connection.commit()

    cursor.close()

    connection.close()
    return {"message": "Product deleted successfully"}