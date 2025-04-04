from flask import Flask, request, render_template_string

app = Flask(__name__)

calculated = "Brak (jeszcze)"

@app.route('/')
def showCalculated():
    return render_template_string("<h1>Wynik sumy Fibonacciego: {{ calculated }}</h1>", calculated=calculated)


@app.route('/result', methods=['POST'])
def update_result():
    global calculated
    data = request.json
    sumFib = data.get('sum')
    calculated = sumFib
    return {"status": "Saved"}

app.run(host='0.0.0.0', port=5000)