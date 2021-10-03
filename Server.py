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
look_back = 30
app = Flask(__name__)

model = keras.models.load_model('ALLSKY_SFC_PAR_TOT_10021210.h5')

print("HI")

def predict(num_prediction, model, allskypar):
    #allskypar = np.ndarray(allskypar)
    #allskypar = allskypar.reshape(-1)
    
    prediction_list = allskypar[-look_back:]
    print(prediction_list)
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
    return ""

@app.route("/")
def hello():
    return ""

@app.route('/api', methods =['GET'])
def api():
    today = datetime.datetime.now()
    veryLongAgo = today - datetime.timedelta(days = 50)
    lat = request.args.get('lat')
    lng = request.args.get('lng')
    days = request.args.get('days')
    URL = 'https://power.larc.nasa.gov/api/temporal/daily/point?parameters=ALLSKY_SFC_PAR_TOT&community=SB&longitude=' + lng + '&latitude=' + lat + '&start=' + veryLongAgo.strftime('%Y%m%d') + '&end=' + today.strftime('%Y%m%d') + '&format=JSON'
    print(URL)

    num_prediction = int(days)

    r = requests.get(url = URL)
    print('get')
    data = r.json()['properties']['parameter']['ALLSKY_SFC_PAR_TOT']
    print('ohno')
    print(data)

    allskypar_array = []
    for key in data:
            allskypar_array.append(int(data[key]))
    print(allskypar_array)
    allskypar = pd.DataFrame(allskypar_array)
    print(allskypar)
    asp = allskypar.to_numpy()
    forecast = predict(num_prediction, model, asp)
    print(forecast)
    res = 0
    for i in range(num_prediction):
        res+=forecast[i]
    return str(res)


if __name__ == '__main__':
    app.debug = True
    app.run()
    #app.run('0.0.0.0', '5000')
