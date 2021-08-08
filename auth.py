from passlib.context import CryptContext
import jwt
from models import User
from dotenv import dotenv_values
from fastapi.exceptions import HTTPException
from fastapi import status

config_credentials = dict(dotenv_values(".env"))



pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gen_hashed_password(password):
    return pwd_context.hash(b"password")


async def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)

async def authenticate_user(username: str, password: str):
    user = await User.get(username=username)

    if user and verify_password(password, user.password):
        return user
    return False

async def token_generator(username: str, password: str):
    user = await authenticate_user(username, password)
    
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Invalid Username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token_data = {
        "id": user.id,
        "username": user.username
    }

    token = jwt.encode(token_data, config_credentials["SECRET"])
    return token

async def verify_token(token: str):
    try:
        payload = jwt.decode(token, config_credentials['SECRET'], algorithms = ['HS256'])
        user = await User.get(id = payload.get('id'))
    except:
        raise HTTPException(
            status_code = status.HTTP_401_UNAUTHORIZED, 
            detail = "Invalid username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )

    return user
