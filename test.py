import yfinance as yf
import matplotlib.pyplot as plt 
from pandas import DataFrame

sp500 = yf.Ticker("^GSPC")
data = sp500.history('ytd')

# Create the plot space upon which to plot the data
fig, ax = plt.subplots()

fig.autofmt_xdate()

# Add the x-axis and the y-axis to the plot
ax.plot(data.index.values,
        data['Close'], '-o',
        color='blue')

ax.plot(data.index.values,
        data['High'], '-o',
        color='green')

ax.plot(data.index.values,
        data['Low'], '-o',
        color='red')
ax.legend(['Close','High','Low'])
# Set title and labels for axes
ax.set(xlabel="Date",
       ylabel="Price",
       title="S&P 500 Close")

plt.savefig('sp500.png')