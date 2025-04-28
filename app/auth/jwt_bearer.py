from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from jose import JWTError, jwt
from typing import Optional
from .crud.get_user import get_user

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

def JWTBearer(user=Depends(get_user), token: Optional[str] = Depends(oauth2_scheme)):
    credential_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Could not validate credentials",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, "YOUR-SECRET-KEY")
        username: str = payload.get("sub")
        if not username:
            raise credential_exception
        token_data = schemas.TokenData(username=username)
    except JWTError:
        raise credential_exception

    return user