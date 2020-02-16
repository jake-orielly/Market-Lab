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
    add_percent(option_df,curr_price)
    add_break_even(option_df)
    max_strike = curr_price + curr_price * percent/100
    min_strike = curr_price - curr_price * percent/100
    matching = option_df.loc[(option_df['strike'] >= min_strike) & (option_df['strike'] <= max_strike),['strike','lastPrice','breakEven','percentOfCurr']]
    return matching

# Adds percent of current price as column
def add_percent(df,curr_price):
    percent = []
    for i in range(len(df)):
        percent.append((df['strike'][i]/curr_price))
    df['percentOfCurr'] = percent 

def add_break_even(df):
    break_even = []
    for i in range(len(df)):
        break_even.append(df['strike'][i] - df['lastPrice'][i])
    df['breakEven'] = break_even 

def get_option_dates(ticker):
    return ticker.options