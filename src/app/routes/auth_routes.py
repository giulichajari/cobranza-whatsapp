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

    # ⚠️ demo (luego lo conectas a DB + bcrypt)
    if username != "admin":
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    if password != "123456":
        raise HTTPException(
            status_code=401,
            detail="Credenciales inválidas"
        )

    token = crear_token({
        "sub": username
    })

    return {
        "access_token": token,
        "token_type": "bearer"
    }