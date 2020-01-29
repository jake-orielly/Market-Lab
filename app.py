from flask import Flask, request
from flask_cors import CORS
import yfinance as yf
from graphing_utilities import compare
import json

sp500 = yf.Ticker("^GSPC")

app = Flask(__name__) 
CORS(app)

@app.route('/compare', methods=['POST'])
def compare_stocks():
    data = json.loads(request.data.decode('utf8'))
    compare(data['stocks'])
    return {'message':'Success'}