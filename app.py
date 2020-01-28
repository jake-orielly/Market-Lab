from flask import Flask
from flask_cors import CORS
import yfinance as yf

sp500 = yf.Ticker("^GSPC")

app = Flask(__name__)
CORS(app)

@app.route('/')
def hello_world():
    return {'results':sp500.history('5d')}