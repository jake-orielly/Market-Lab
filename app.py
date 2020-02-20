from flask import Flask, request
from flask_cors import CORS
import json

from graphing_utilities import compare
from options_utilities import get_within_percent, get_curr_price

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
    curr_price = get_curr_price(data['tickerName'])
    return {'message':'Success','data':matching.to_json(),'curr_price':curr_price}