from flask import Flask, request, render_template_string, Response
import threading

app = Flask(__name__)

calculated = "Brak (jeszcze)"
event = threading.Event()

@app.route('/')
def showCalculated():
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


@app.route('/result', methods=['POST'])
def update_result():
    global calculated
    data = request.json
    calculated = data.get('sum')
    event.set()
    return {"status": "Saved"}

@app.route('/stream')
def stream():
    def event_stream():
        while True:
            event.wait()
            yield 'data: refreshed\n\n'
            event.clear()
    return Response(event_stream(), mimetype="text/event-stream")

app.run(host='0.0.0.0', port=5000)