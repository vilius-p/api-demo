from fastapi import FastAPI

import requests

app = FastAPI()


@app.get("/hello")
async def hello():
    return "Hello Telia"


@app.get("/quote")
async def get_quote():
    # response = requests.get("https://zenquotes.io/api/today")
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch the quote"}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8000)
