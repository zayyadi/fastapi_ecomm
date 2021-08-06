from fastapi import (BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from pydantic import BaseModel, EmailStr
from typing import List

config_credentials = (".env")
conf = ConnectionConfig(
    MAIL_USERNAME = config_credentials["EMAIL"],
    MAIL_PASSWORD = config_credentials["PASS"],
    MAIL_FROM = config_credentials["EMAIL"],
    MAIL_PORT = "",
    MAIL_SERVER = "smtp.ipage.com",
    MAIL_TLS= True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
)


class EmailSchema(BaseModel):
    email: List[EmailStr]
