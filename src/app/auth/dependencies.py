from fastapi import Depends, HTTPException
from fastapi.security import OAuth2PasswordBearer

from jose import jwt, JWTError

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/auth/login"
)

SECRET_KEY = "tu_clave_super_secreta"
ALGORITHM = "HS256"


def get_current_user(
    token: str = Depends(oauth2_scheme)
):
    try:
        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Token inválido"
            )

        return username
    except JWTError:
        raise HTTPException(
            status_code=401,
            detail="Token inválido"
        )
