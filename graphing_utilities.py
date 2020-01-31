import yfinance as yf
import matplotlib.pyplot as plt 
from pandas import DataFrame

from calculation_utilities import add_percent_change

colors = ['blue','green','red','cyan','magenta','yellow','black','white']
time_ranges = ['1d','5d','1mo','3mo','6mo','1y','2y','5y','10y','ytd','max']

def compare(stocks,time):
    # Create the plot space upon which to plot the data
    fig, ax = plt.subplots()
    fig.autofmt_xdate()
    
    tickers = []
    for i in range(len(stocks)):
        tickers.append(yf.Ticker(stocks[i]))
        data = tickers[-1].history(time)
        add_percent_change(data)
        ax.plot(data.index.values, data['Change'], '-o', markersize=0.1, color=colors[i % len(colors)])

    ax.legend(stocks)

    # Set title and labels for axes
    ax.set(xlabel='Date',
    ylabel='Price',
    title='Close Price')

    plt.savefig('results.png')