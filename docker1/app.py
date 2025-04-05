from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route('/input', methods=['POST'])
def input_data():
    data = request.json
    integer = data.get('integer')
    
    if integer is None:
        return jsonify({"error": "Did not get an integer"}), 400
    print(f"Integer = {integer}")
    
    response = requests.post('http://docker2:5000/submit-task', json={"integer": integer})
    return jsonify({"status": "Sent to Docker 2", "Docker2Response": response.json()})

app.run(host='0.0.0.0', port=5000)