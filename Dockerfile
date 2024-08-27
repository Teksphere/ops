FROM python:3.9-slim

WORKDIR /app

COPY echo_server.py .
COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

ENTRYPOINT ["python", "echo_server.py"]
