from fastapi import APIRouter, HTTPException, Form, Request
from Database.dbGetConnection import getConnectionForLogin
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse
from typing import Annotated

router = APIRouter()

jinja2Templates = Jinja2Templates(directory="venv/Templates")

def authenticate_user(username: str, password: str):
    connection = getConnectionForLogin()
    cursor = connection.cursor(dictionary=True)
    cursor.execute("SELECT * FROM credentials WHERE username = %s AND password = %s", (username, password))
    user = cursor.fetchone()
    cursor.close()
    connection.close()
    return user

@router.get('/admin', response_class=HTMLResponse)
def login(request: Request):
    return jinja2Templates.TemplateResponse("index.html", {"request": request})

@router.post('/login')
def login(request: Request, username: Annotated[str, Form()], password: Annotated[str, Form()]):
    user = authenticate_user(username, password)
    if user:
        return RedirectResponse(url="/dashboard", status_code=303)
    else:
        return RedirectResponse(url="/failed-login", status_code=303)

@router.get('/dashboard', response_class=HTMLResponse)
def dashboard(request: Request):
    return jinja2Templates.TemplateResponse("dashboard.html", {"request": request})

@router.get('/failed-login', response_class=HTMLResponse)
def failed_login(request: Request):
    return jinja2Templates.TemplateResponse("failedLogin.html", {"request": request})