from flask import Flask
from flask import json
import pandas as pd

app = Flask(__name__)

@app.route('/api/v1/airports')
def airports():
    df = pd.read_csv('examples-data/airports.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/flightdata')
def flightdata():
    df = pd.read_csv('examples-data/flight_data.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/birthfrance')
def birthfrance():
    df = pd.read_csv('examples-data/birth_france_data_for_country_map.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/tutorialflights')
def tutorialflights():
    df = pd.read_csv('examples-data/tutorial_flights.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/videogamesales')
def videogamesales():
    df = pd.read_csv('examples-data/datasets/examples/video_game_sales.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

@app.route('/api/v1/sales')
def sales():
    df = pd.read_csv('examples-data/datasets/examples/sales.csv')
    response = app.response_class(
        response = df.to_json(orient="records"),
        status=200,
        mimetype='application/json'
    )
    return response

if __name__ == '__main__':
    # app.run(host='0.0.0.0', port=80)
    app.run()