from passlib.context import CryptContext

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')


def gen_hashed_password(password):
    return pwd_context.hash(b"password")
