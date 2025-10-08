from fastapi import Depends , Header, HTTPException
from app.core.config import get_settings
from app.core.security import verify_token

def get_api_key(api_key: str = Header(...), settings=Depends(get_settings)):
    if api_key != settings.API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    return api_key

def get_current_user(token: str = Header(...)):
    payload = verify_token(token)
    if payload is None:
        raise HTTPException(status_code=401, detail="Invalid or expired token")
    return payload


