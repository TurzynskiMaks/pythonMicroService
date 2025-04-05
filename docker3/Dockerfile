FROM python:3.11-slim

WORKDIR /app

COPY . .

RUN pip install flask redis

CMD ["python", "app.py"]
