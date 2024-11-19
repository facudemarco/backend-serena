from fastapi import FastAPI
import uvicorn
from models.product import Product
from routers.product import router as routerProduct
from routers.login import router as routerLogin

app = FastAPI()

@app.get('/')
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(routerLogin)

app.include_router(routerProduct)