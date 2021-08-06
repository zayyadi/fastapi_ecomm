from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from models import *
from auth import gen_hashed_password

#signal
from tortoise.signals import post_save
from typing import List, Optional, Type
from tortoise import BaseDBAsyncClient

app = FastAPI()

@post_save(User)
async def create_business(
    sender: "Type[User]",
    instance: User,
    created: bool,
    using_db: "Optional[BaseDBAsyncClient]",
    updated_fileds: List[str]
) -> None:

    if created:
        business_obj = await Business.create(
            business_name=instance.username, owner=instance
        )
        await business_pydantic.from_tortoise_orm(business_obj)



@app.post("/register")
async def register(user: user_pydanticIn):
    user_info = user.dict(exclude_unset=True)
    user_info["password"]= gen_hashed_password([user_info["password"]])
    user_obj = await User.create(**user_info)
    new_user = await user_pydantic.from_tortoise_orm(user_obj)
    return {
        "status": "success",
        "data": f"Hello {new_user.username}, thanks for choosing our services. Please check your email to verify your email."
    }



@app.get("/")
def index():
    return {"Message": "Hello world"}


register_tortoise(
    app,
    db_url="sqlite:db.sqlite",
    modules={"models": ["models"]},
    generate_schemas=True,
    add_exception_handlers=True,
)