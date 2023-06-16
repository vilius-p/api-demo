# FROM python:3.9.17-slim-bullseye
FROM python:3.9.1-alpine

WORKDIR /app

COPY src src
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN ls -la . && pwd && ls -la /app

CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8000"]
