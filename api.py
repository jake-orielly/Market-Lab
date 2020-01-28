import yfinance as yf
from flask import Flask

tsla = yf.Ticker("TSLA")
print(tsla.history(period="5d"))

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'