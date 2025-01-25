from fastapi import APIRouter, HTTPException, Form, Request
from Database.dbGetConnection import getConnectionForLogin
from fastapi.responses import JSONResponse, RedirectResponse
from typing import Annotated

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

@router.get('/admin', response_class=JSONResponse, summary="Página de Inicio de Sesión", description="Endpoint que indica que la página de inicio de sesión está disponible.")
def login_admin(request: Request):
    """
    Este endpoint indica que la página de inicio de sesión está disponible.
    Se debe renderizar la página de inicio de sesión cuando se acceda a este endpoint.
    """
    return JSONResponse(content={"message": "Inicio de sesión disponible"}, status_code=200)

@router.post('/login', response_class=JSONResponse, summary="Inicio de Sesión de Usuario", description="Endpoint para el inicio de sesión del usuario. La respuesta indica la página a renderizar en caso de éxito o fracaso.")
def login(username: Annotated[str, Form(description="Nombre de usuario")], password: Annotated[str, Form(description="Contraseña")]):
    """
    Este endpoint maneja el inicio de sesión del usuario.
    - En caso de inicio de sesión exitoso, devuelve un mensaje con una URL de redirección para el dashboard.
    - En caso de fallo en el inicio de sesión, devuelve un mensaje con una URL de redirección para la página de inicio de sesión fallido.
    """
    user = authenticate_user(username, password)
    if user:
        return JSONResponse(content={"message": "Inicio de sesión exitoso", "redirect_url": "/dashboard"}, status_code=200)
    else:
        return JSONResponse(content={"message": "Inicio de sesión fallido", "redirect_url": "/failed-login"}, status_code=401)

@router.get('/dashboard', response_class=JSONResponse, summary="Dashboard", description="Endpoint que indica la página del dashboard.")
def dashboard(request: Request):
    """
    Este endpoint indica la página del dashboard.
    Se debe renderizar la página del dashboard cuando se acceda a este endpoint.
    """
    return JSONResponse(content={"message": "Bienvenido al dashboard", "data": {"key": "value"}}, status_code=200)

@router.get('/failed-login', response_class=JSONResponse, summary="Inicio de Sesión Fallido", description="Endpoint que indica la página de inicio de sesión fallido.")
def failed_login(request: Request):
    """
    Este endpoint indica la página de inicio de sesión fallido.
    Se debe renderizar la página de inicio de sesión fallido cuando se acceda a este endpoint.
    """
    return JSONResponse(content={"message": "Inicio de sesión fallido"}, status_code=401)
