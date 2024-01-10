import requests
from fastapi import APIRouter, Depends

from .src.conf.config import settings
from .src.db import db
from .src.schemas.email import PersonModel, EmailVerify, Email


router = APIRouter(prefix="/email", tags=["email"])


@router.get("/find", name="Return email if find person", response_model=Email)
async def find_email(body: PersonModel = Depends()):

    params = dict(body)
    params["api_key"] = settings.api_hunter_io
    url = f"https://api.hunter.io/v2/email-finder"
    response = requests.get(url=url, params=params)
    email = response.json().get("data", {}).get("email", "Not found")

    return {"email": email}


@router.get("/verify", name="Returns the email verification status", response_model=EmailVerify)
async def verify_email(body: Email = Depends()):

    params = {
        "email": body.email,
        "api_key": settings.api_hunter_io
    }
    url = f"https://api.hunter.io/v2/email-verifier"
    response = requests.get(url=url, params=params)
    db.result = response.json()
    status = db.result.get("data", {}).get("status", "Not found")

    return {"status": status}