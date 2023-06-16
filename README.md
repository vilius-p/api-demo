# API Demo

This demo is made to showcase a basic API microservice written in python, using FastAPI and Uvicorn. The API includes monitoring, visualized on a grafana dashboard.

[API](http://telia.demo.vilius.xyz)
![build](https://github.com/vilius-p/api-demo/actions/workflows/image-publish/badge.svg)
[Grafana](https://grafana.demo.vilius.xyz/)


## Prerequisites

- docker-compose

## Endpoints

- GET /hello: Returns "Hello Telia. Limited to 5/min

- GET /quote: Returns random quote JSON. Limited to 10/min

- GET /health: Returns if service is healthy. Limited to 5/min

- GET /metrics: Returns metrics for prometheus.



## Quick start

To call the endpoints:
```
curl -L telia.demo.vilius.xyz/hello
```
```
curl -L telia.demo.vilius.xyz/quote
```

## Local implementation
It is possible to run the solution locally. For this please modify:
```
grafana_data/grafana.ini
```
Where 
```
domain = <YOUR_DOMAIN.COM>
```

To build solution locally:
```
docker-compose up -d
```