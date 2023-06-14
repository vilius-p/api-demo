from fastapi import FastAPI
from prometheus_client import start_http_server, Summary

import requests

app = FastAPI()
request_time = Summary("request_processing_seconds", "Time spent processing request")


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


@app.get("/health")
def get_health():
    return {"status": "healthy"}


@app.get("/metrics")
def get_metrics():
    # Expose Prometheus metrics
    return Response(prometheus_client.generate_latest(), media_type="text/plain")


if __name__ == "__main__":
    import uvicorn

    start_http_server(8001)

    uvicorn.run(app, host="0.0.0.0", port=8000)
