from celery import Celery
import redis
import requests

app = Celery('worker', broker='redis://redis:6379/0')

redisClient = redis.Redis(host='redis', port=6379, decode_responses=True)

@app.task
def calculateFib(n):
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    sumFib = sum(sequence)
    
    redisClient.set('fibonacciSum', sumFib)
    print(f'Sent to redis!')
    
    requests.post('http://docker3:5000/result', json={'sum': sumFib})