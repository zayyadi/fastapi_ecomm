from passlib.context import CryptContext
import jwt
from .models import User
from dotenv import dotenv_values
from fastapi.exceptions import HTTPException
from fastapi import status

config_credentials = dotenv_values(".env")



pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gen_hashed_password(password):
    return pwd_context.hash(b"password")


async def verify_token(token: str):
    try:
        payload = jwt.decode(token, config_credentials["SECRET"])
        user = await User.get(id = payload.get("id"))

    except:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid token",
            headers={"WWW-Authenticate": "Bearer"}

        )
    return user
