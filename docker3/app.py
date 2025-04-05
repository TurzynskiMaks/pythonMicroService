from flask import Flask, request, render_template_string, Response
import redis
import threading

app = Flask(__name__)

redisClient = redis.Redis(host='redis', port=6379, decode_responses=True)
event = threading.Event()

@app.route('/')
def showCalculated():
    calculated = redisClient.get('fibonacciSum') or "Brak wyniku (jeszcze)"
    return render_template_string("""
        <html>
            <head>
                <title>Wynik Fibonacciego</title>
                <script>
                    var source = new EventSource("/stream");
                    source.onmessage = function(event) {
                        location.reload();
                    };
                </script>
            </head>
            <body>
                <h1>Wynik sumy Fibonacciego: {{ result }}</h1>
            </body>
        </html>
    """, result=calculated)

@app.route('/trigger-refresh', methods=['POST'])
def triggerRefresh():
    event.set()
    return {"status": "Frontend refresh triggered"}

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            event.wait()
            yield 'data: refreshed\n\n'
            event.clear()
    return Response(event_stream(), mimetype="text/event-stream")

app.run(host='0.0.0.0', port=5000)