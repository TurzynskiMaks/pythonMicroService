from flask import Flask, request, jsonify
import requests

app = flask(__name__)

@app.route('/input', methods=['POST'])
def input_data():
    data = request.json
    integer = data.get('integer')
    
    if integer is None:
        return jsonify({"error": "Did not get an integer"}), 400
    
    
    response = requests.post('http://docker2:5000/fib', json={"integer": integer})
    return jsonify({"status": "Send to Docker 2", "Docker2Response": response.json()})
app.run(host='0.0.0.0', port=5000)