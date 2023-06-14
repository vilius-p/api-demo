from fastapi import FastAPI, Response
from prometheus_fastapi_instrumentator import Instrumentator
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


@app.get("/health")
def get_health():
    return {"status": "healthy"}


# @app.get("/metrics")
# def get_metrics():
#     # Expose Prometheus metrics
#     # return Response(prometheus_client.generate_latest(), media_type="text/plain")
#     return generate_latest(metrics_reg)


if __name__ == "__main__":
    import uvicorn

    Instrumentator().instrument(app).expose(app)

    uvicorn.run(app, host="0.0.0.0", port=8000)
