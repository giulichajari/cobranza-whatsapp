from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from src.app.auth.jwt import crear_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    username = form_data.username
    password = form_data.password

    if username != "admin":
        raise HTTPException(401, "Credenciales inválidas")

    if password != "123456":
        raise HTTPException(401, "Credenciales inválidas")

    token = crear_token({"sub": username})

    return {
        "access_token": token,
        "token_type": "bearer"
    }