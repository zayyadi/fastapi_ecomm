from fastapi import (BackgroundTasks, UploadFile, File, Form, Depends, HTTPException, status)
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig
from dotenv import dotenv_values
from pydantic import BaseModel, EmailStr
from typing import List
from models import User
import jwt




config_credentials = dict(dotenv_values(".env"))
conf = ConnectionConfig(
    MAIL_USERNAME = '1902ec824c2953',
    MAIL_PASSWORD = '7365f34d9afdd9',
    MAIL_FROM = "email1@emaple.com",
    MAIL_PORT = 2525,
    MAIL_SERVER = "smtp.mailtrap.io",
    MAIL_TLS= True,
    MAIL_SSL = False,
    USE_CREDENTIALS = True,
)



async def send_email(email:List, instance: User):

    token_data = {
        "id": instance.id,
        "username": instance.username
    }

    token = jwt.encode(token_data, config_credentials["SECRET"], algorithm='HS256')

    template = f"""
    <!DOCTYPE html>
    <html>
        <head>
        </head>
        <body>
            <div styke="display: flex; align-items: center; justify-content: center; flex-direction: column">
                <h3>Account Verification</h3>
                <br>

                <p> Thanks for choosing Zhop, Please click on the button below to verify your account </p>

                <a style="margin-top: 1rem; padding: 1rem; border-radius: 0.5rem; font-size: 1rem; text-decoration: none; background: #0275d8; color: white;" href="http://localhost:8000/verification/?token={token}">Verify</a>
                <p> Please kindly ignore this email if you didn't register for Zhop</p>
            </div>
        </body>
    </html>

    """
    message = MessageSchema(
        subject = "Zhop account Verification Email",
        recipients = email,
        body = template,
        subtype = "html" 
    )

    fm = FastMail(conf)
    await fm.send_message(message=message)