from flask import Flask, request
from flask_cors import CORS
import json

import numpy as np

from graphing_utilities import compare
from options_utilities import get_within_percent, get_curr_price, get_option_dates

app = Flask(__name__) 
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_stocks():
    data = json.loads(request.data.decode('utf8'))
    compare(data['stocks'],data['period'],data['interval'])
    return {'message':'Success'}

@app.route('/options_info', methods=['POST'])
def options_info():
    data = json.loads(request.data.decode('utf8'))
    matching = get_within_percent(data['tickerName'],data['date'],data['percent'],data['contractType'])
    matching_list = np.rot90(np.fliplr(matching.to_numpy())).tolist()
    matching_json = json.dumps(matching_list)
    curr_price = get_curr_price(data['tickerName'])
    return {'message':'Success','data':matching_json,'curr_price':curr_price,'columns':list(matching.columns)}

@app.route('/options_dates',methods=['POST'])
def options_dates():
    req_data = request.data.decode('utf8')
    req_data = json.loads(req_data)
    return {'dates':get_option_dates(req_data['tickerName'])}