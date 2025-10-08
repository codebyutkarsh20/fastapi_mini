from fastapi import APIRouter
from app.core.security import create_token
from pydantic import BaseModel

router = APIRouter()

class TokenRequest(BaseModel):
    username: str
    password: str


@router.post("/login")
def login(request: TokenRequest):
    # In a real application, you would verify the username and password
    if request.username == "admin" and request.password == "password":
        token = create_token({"sub": request.username})
        return {"access_token": token}
    else:
        return {"error": "Invalid credentials"}