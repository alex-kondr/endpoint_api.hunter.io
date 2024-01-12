from fastapi import FastAPI
import uvicorn

try:
    from src.routes import find_verify_email, result
except ModuleNotFoundError:
    from .src.routes import find_verify_email, result


app = FastAPI()
app.include_router(find_verify_email.router)
app.include_router(result.router)


def start():
    uvicorn.run("endpoint_api_hunter_io.main:app", host="0.0.0.0", port=8000, reload=True)
