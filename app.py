import flask
from flask import request, jsonify

app = flask.Flask(__name__)
# app.config["DEBUG"] = True

@app.route('/', methods=['GET'])
def home():
    return "Api de Conversão em Python-v3"


@app.route('/celsius/<int:temperatura>/fahrenheit', methods=['GET'])
def celsius_fahrenheit(temperatura=None):
    fahrenheit = (temperatura * 9 / 5) + 32
    return jsonify({ 'fahrenheit': fahrenheit })

@app.route('/fahrenheit/<int:temperatura>/celsius', methods=['GET'])
def fahrenheit_celsius(temperatura=None):
    celsius = (temperatura - 32) * 5 / 9
    return jsonify({ 'celsius': celsius })

if __name__ == '__main__':
    app.run()
