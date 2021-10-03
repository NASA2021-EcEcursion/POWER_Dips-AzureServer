from flask import Flask, request
import pandas as pd
import numpy as np
import keras
import tensorflow as tf
from keras.preprocessing.sequence import TimeseriesGenerator
from keras.models import Sequential
from keras.layers import LSTM, Dense
import requests
import datetime
import json

app = Flask(__name__)

model = keras.models.load_model('ALLSKY_SFC_PAR_TOT_10021210.h5')

print("HI")

def predict(num_prediction, model):
    prediction_list = allskypar[-look_back:]

    for _ in range(num_prediction):
        x = prediction_list[-look_back:]
        x = x.reshape((1, look_back, 1))
        out = model.predict(x)[0][0]
        prediction_list = np.append(prediction_list, out)
    prediction_list = prediction_list[look_back-1:]

    return prediction_list

def predict_dates(num_prediction):
    last_date = df['INDEX'].values[-1]
    prediction_dates = pd.date_range(last_date, periods=num_prediction+1).tolist()
    return prediction_dates

@app.route("/")
def hello():
    return "Hello, World1!"

@app.route('/api', methods =['GET'])
def api():
    today = datetime.datetime.now()
    veryLongAgo = today - datetime.timedelta(days = 50)
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    days = request.args.get('days')
    URL = 'https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_PAR_TOT&community=SB&longitude=' + lng + '&latitude=' + lat + '&start=' + veryLongAgo.strftime('%Y%m%d') + '&end=' + today.strftime('%Y%m%d') + '&format=JSON'
    print(URL)

    r = requests.get(url = URL)
    print('get')
    data = r.json

    print('ohno')
    print(data)
    
    print(json.dumps(data))

    forecast = predict(days, model)

    return "Hello" + json.dumps(data)

if __name__ == '__main__':
    app.debug = True
    app.run('0.0.0.0', '5000')
