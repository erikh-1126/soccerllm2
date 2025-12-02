FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY src/ ./src
COPY models/ ./models

ENV MODEL_PATH=/app/models/llama-3-8b-q4.gguf

CMD ["python", "src/app.py"]
