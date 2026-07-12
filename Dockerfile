FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN mkdir -p data

CMD ["python", "app.py"]