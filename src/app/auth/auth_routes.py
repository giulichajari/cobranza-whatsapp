from fastapi import APIRouter, HTTPException

from src.app.auth.jwt import crear_token

router = APIRouter(
    prefix="/auth",
    tags=["Auth"]
)


@router.post("/login")
def login(username: str, password: str):

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