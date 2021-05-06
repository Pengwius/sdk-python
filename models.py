from pydantic import BaseModel
from typing import Optional, Any
import json

class LoginModel(BaseModel):
    login: str
    password: str
    symbol: str
    journal: str

class UserModel(BaseModel):
    expiration_date: float
    key: bytes

class RequestBodyModel(BaseModel):
    register_id: int
    school_url: str
    student: dict
    cookies: str