from datetime import datetime, timedelta , timezone
from typing import Optional
from jose import JWTError, jwt
from passlib.context import CryptContext
from app.core.config import get_settings

settings = get_settings()

def create_token(data:dict , expire_minuts=30):
    to_encode = data.copy()
    expire = datetime.now(timezone.utc) + timedelta(minutes=expire_minuts)
    to_encode.update({"exp":expire})
    return jwt.encode(to_encode, settings.JWT_SECRET_KEY, algorithm=settings.JWT_ALGORITHM)

def verify_token(token:str):
    try: 
        payload = jwt.decode(token,settings.JWT_SECRET_KEY,algorithm=settings.JWT_ALGORITHM)
        return payload if payload.get("exp") >= datetime.now(timezone.utc).timestamp() else None
    except JWTError:
        return None