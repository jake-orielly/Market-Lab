import yfinance as yf
import matplotlib.pyplot as plt 
from pandas import DataFrame

from calculation_utilities import add_percent_change, add_rsi
from filter_df import filter_df

colors = ['blue','green','red','cyan','magenta','yellow','black','white']

def compare(stocks,period,interval):
    # Create the plot space upon which to plot the data
    fig, ax1 = plt.subplots()
    fig.autofmt_xdate()
    
    tickers = []
    for i in range(len(stocks)):
        tickers.append(yf.Ticker(stocks[i]))
        history = tickers[-1].history(period=period,interval=interval)
        add_percent_change(history)
        add_rsi(history,14)
        ax1.plot(history.index.values, history['Change'], linewidth=1, color=colors[i % len(colors)])
        nh = filter_df(history,'RSI','>',80)
        for i in range(len(nh.index.values)):
            ax1.axvspan(nh.index.values[i], nh.index.values[i], linewidth=1, color='red', alpha=0.5)

        ax2 = ax1.twinx()

        ax2.set_ylabel('RSI')
        ax2.plot(history.index.values, history['RSI'], linewidth=1, linestyle=':', color=colors[i % len(colors)])
    #ax1.plot('2020-01-22',10,color="purple")
    # Otherwise the right y-label gets clipped
    fig.tight_layout()  
    ax1.legend(stocks)

    # Set title and labels for axes
    ax1.set(xlabel='Date',
    ylabel='Price')

    plt.savefig('results.png')

