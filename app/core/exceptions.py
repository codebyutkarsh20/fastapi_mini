from fastapi import Request, HTTPException , FastAPI
from fastapi.responses import JSONResponse



def register_exception_handlers(app:FastAPI):
    @app.exception_handler(Exception)
    async def generic_exception_handler(request:Request, exc:Exception):
        return JSONResponse(status_code=500, content={"message": "str(exc)"},)
    