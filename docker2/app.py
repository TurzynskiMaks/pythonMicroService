from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

def fibonacci(n):
    sequence = [1,1]
    while len(sequence) < n:
        sequence.append(sequence[-1] + sequence[-2])
    return sequence[:n]

@app.route('/fib', methods=['POST'])

def calculateFib():
    data = request.json
    integer = int(data.get('integer'))
    fib = fibonacci(integer)
    sumFib = sum(fib)
    
    requests.post('http://docker3:5000/result', json={'sum': sumFib})
    
    return jsonify({"fib": fib, "sum": sumFib})

app.run(host='0.0.0.0', port=5000)