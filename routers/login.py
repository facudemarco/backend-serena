from fastapi import APIRouter, HTTPException, Form, Request, Depends
from fastapi.responses import JSONResponse, RedirectResponse, Response
from typing import Annotated, cast
from datetime import datetime, timedelta
from jose import jwt, JWTError
from Database.dbGetConnection import getConnectionForLogin
from dotenv import load_dotenv
import os

load_dotenv()
SECRET = os.getenv("SECRET_KEY")
if not SECRET:
    raise ValueError("SECRET_KEY environment variable is not set")
SECRET_KEY = cast(str, SECRET)
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_DAYS = 30

router = APIRouter()

def authenticate_user(username: str, password: str):
    connection = getConnectionForLogin()
    if not connection:
        return None

    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM `credentials` WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

def create_access_token(data: dict):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(days=ACCESS_TOKEN_EXPIRE_DAYS)
    to_encode.update({"exp": expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt

def get_current_user(request: Request):
    token = request.cookies.get("access_token")
    if not token:
        return None
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username = payload.get("username")
        if username is None:
            return None
        return {"username": username}
    except JWTError:
        return None

@router.get('/admin', response_class=JSONResponse, summary="Página de Inicio de Sesión", description="Endpoint que indica que la página de inicio de sesión está disponible.")
def login_admin(request: Request):
    return JSONResponse(content={"message": "Inicio de sesión disponible"}, status_code=200)

@router.post('/login', response_class=JSONResponse, summary="Inicio de Sesión de Usuario", description="Endpoint para el inicio de sesión del usuario. La respuesta indica la página a renderizar en caso de éxito o fracaso.")
def login(response: Response, username: Annotated[str, Form(description="Nombre de usuario")], password: Annotated[str, Form(description="Contraseña")]):
    user = authenticate_user(username, password)
    if user:
        access_token = create_access_token(data={"username": username})
        response.set_cookie(key="access_token", value=access_token, httponly=True, secure=False, samesite="lax", max_age=ACCESS_TOKEN_EXPIRE_DAYS * 24 * 60 * 60)
        return JSONResponse(content={"message": "Inicio de sesión exitoso", "redirect_url": "/dashboard"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Inicio de sesión fallido", "redirect_url": "/failed-login"}, status_code=401)

@router.get('/dashboard', response_class=JSONResponse, summary="Dashboard", description="Endpoint que indica la página del dashboard.")
def dashboard(request: Request, current_user: dict | None = Depends(get_current_user)):
    if current_user:
        return JSONResponse(content={"message": f"Bienvenido al dashboard, {current_user['username']}", "data": {"key": "value"}}, status_code=200)
    else:
        return JSONResponse(content={"message": "No autorizado", "redirect_url": "/"}, status_code=401)

@router.get('/failed-login', response_class=JSONResponse, summary="Inicio de Sesión Fallido", description="Endpoint que indica la página de inicio de sesión fallido.")
def failed_login(request: Request):
    return JSONResponse(content={"message": "Inicio de sesión fallido"}, status_code=401)

@router.get('/', response_class=JSONResponse, summary="Página Principal", description="Endpoint para la página principal.")
def index(request: Request):
    return JSONResponse(content={"message": "Bienvenido a la página principal"}, status_code=200)

@router.get('/logout', response_class=JSONResponse, summary="Cerrar Sesión", description="Endpoint para cerrar la sesión del usuario.")
def logout(response: Response):
    response.delete_cookie("access_token")
    return JSONResponse(content={"message": "Sesión cerrada exitosamente", "redirect_url": "/"}, status_code=200)