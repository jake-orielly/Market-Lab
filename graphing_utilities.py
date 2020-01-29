import yfinance as yf
import matplotlib.pyplot as plt 
from pandas import DataFrame

colors = ['blue','green','red','cyan','magenta','yellow','black','white']

def compare(stocks):
    # Create the plot space upon which to plot the data
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    
    tickers = []
    for i in range(len(stocks)):
        tickers.append(yf.Ticker(stocks[i]))
        data = tickers[-1].history('ytd')
        ax.plot(data.index.values, data['Close'], '-o',color=colors[i % len(colors)])

    ax.legend(stocks)

    # Set title and labels for axes
    ax.set(xlabel='Date',
    ylabel='Price',
    title='Close Price')

    plt.savefig('results.png')