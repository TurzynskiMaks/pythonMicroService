FROM python:3.11-slim

WORKDIR /app
COPY . .

RUN pip install flask requests redis celery

CMD ["celery", "-A", "worker", "worker", "--loglevel=info", "--pool=solo"]