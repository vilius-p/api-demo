from fastapi import FastAPI, Response
from prometheus_client import (
    Counter,
    Histogram,
    start_http_server,
    generate_latest,
    CollectorRegistry,
)
import requests

metrics_reg = CollectorRegistry()
num_q = CollectorRegistry(
    "api_num_queries", "counts number of requests sent to API", ["endpoint"]
)
num_err = CollectorRegistry("api_num_errors", "counts number of errors occurred")
latency = Histogram("api_latency", "latency calculator")
# num_q = Counter('api_num_queries','counts number of requests sent to API', ['endpoint'])
# num_err = Counter('api_num_errors','counts number of errors occurred')
# latency = Histogram('api_latency', 'latency calculator')

app = FastAPI()


@app.get("/hello")
@latency.time()
@num_err.count_exceptions()
async def hello():
    return "Hello Telia"


@app.get("/quote")
@latency.time()
@num_err.count_exceptions()
async def get_quote():
    # response = requests.get("https://zenquotes.io/api/today")
    response = requests.get("https://zenquotes.io/api/random")
    if response.status_code == 200:
        return response.json()
    else:
        return {"error": "Failed to fetch the quote"}


@app.get("/health")
@latency.time()
@num_err.count_exceptions()
def get_health():
    return {"status": "healthy"}


@app.get("/metrics")
@latency.time()
@num_err.count_exceptions()
def get_metrics():
    # Expose Prometheus metrics
    # return Response(prometheus_client.generate_latest(), media_type="text/plain")
    return generate_latest(metrics_reg)

if __name__ == "__main__":
    import uvicorn

    start_http_server(8001)

    uvicorn.run(app, host="0.0.0.0", port=8000)
