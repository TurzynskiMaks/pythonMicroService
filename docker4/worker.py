from celery import Celery
import requests

app = Celery('worker', broker='redis://redis:6379/0')


@app.task
def calculateFib(n):
    sequence = [1, 1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    
    sumFib = sum(sequence)
    
    requests.post('http://docker3:5000/result', json={'sum': sumFib})