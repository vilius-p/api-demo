from fastapi import FastAPI

# from fastapi_utils.middleware import RateLimitMiddleware
import requests

# from slowapi import Limiter, _rate_limit_exceeded_handler
# from slowapi.util import get_remote_address
# from slowapi.errors import RateLimitExceeded

# limiter = Limiter(key_func=get_remote_address)
app = FastAPI()
# app.state.limiter = limiter
# app.add_exception_handler(RateLimitExceeded, _rate_limit_exceeded_handler)


@app.get("/hello")
# @limiter.limit("5/minute")
# async def hello(request: Request):
async def hello():
    return "Hello Telia"


@app.get("/quote")
# @limiter.limit("5/minute")
# async def get_quote(request: Request, response: Response):
async def get_quote():
    # response = requests.get("https://zenquotes.io/api/today")
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        # return response.json()[0]["q"]
        return response.json()
    else:
        return {"error": "Failed to fetch the quote"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
