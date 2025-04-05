FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask requests celery redis

CMD ["python", "app.py"]
