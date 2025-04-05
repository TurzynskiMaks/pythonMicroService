from flask import Flask, request, jsonify
from celery import Celery

app = Flask(__name__)


celeryApp = Celery('tasks', broker='redis://redis:6379/0')


@app.route('/submit-task', methods=['POST'])
def submitTask():
    data = request.json
    integer = int(data.get('integer'))
    
    celeryApp.send_task('worker.calculateFib', args=[integer])
    
    return jsonify({"status": "Task submitted to Celery!"})

app.run(host='0.0.0.0', port=5000)