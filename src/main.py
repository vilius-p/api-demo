from fastapi import FastAPI, Response, Request
from prometheus_fastapi_instrumentator import Instrumentator
import requests

from slowapi import Limiter, _rate_limit_exceeded_handler
from slowapi.util import get_remote_address
from slowapi.errors import RateLimitExceeded

limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
app.state.limiter = limiter
app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)

Instrumentator().instrument(app).expose(app)

@app.get("/hello")
@limiter.limit("5/minute")
async def hello(request: Request):
    return "Hello Telia"


@app.get("/quote")
@limiter.limit("10/minute")
async def get_quote(request: Request, response: Response):
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch the quote"}


@app.get("/health")
@limiter.limit("5/minute")
def get_health(request: Request):
    return {"status": "healthy"}


if __name__ == "__main__":
    import uvicorn

    Instrumentator().instrument(app).expose(app)

    uvicorn.run(app, host="0.0.0.0", port=8000)
