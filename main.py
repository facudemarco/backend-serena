from fastapi import FastAPI
import uvicorn
from models.product import Product
from routers.product import router as routerProduct
from routers.login import router as routerLogin
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

origins = [
    "http://localhost:3000",
    "https://serenaviajes.com",
    "https://serena-website.vercel.app/",
    "htpps://hostinger.com"
    "https://serena-website.vercel.app/nacionales"
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/')
def read_root():
    return {"message": "Hello World"}

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)

app.include_router(routerLogin)

app.include_router(routerProduct)