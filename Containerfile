FROM python:3.9.17-slim-bullseye

WORKDIR /app

COPY src .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


CMD ["uvicorn", "scr.main:app", "--host", "0.0.0.0", "--port", "8000"]
