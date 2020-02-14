import yfinance as yf
from pandas import DataFrame

def get_option_chain(ticker,date,contractType):
    if contractType == 'call':
        contractType = 0
    elif contractType == 'put':
        contractType = 1
    else:
        raise Exception('Bad contract type', contractType)
    chain = ticker.option_chain(date)[contractType]
    return chain

def get_within_percent(tickerName,date,percent,contractType):
    ticker = yf.Ticker(tickerName)
    option_df = get_option_chain(ticker,date,contractType)
    curr_price = ticker.history('1d')['Close'][0]
    max_strike = curr_price + curr_price * percent/100
    min_strike = curr_price - curr_price * percent/100
    matching = option_df.loc[(option_df['strike'] >= min_strike) & (option_df['strike'] <= max_strike),['strike','lastPrice']]
    return matching