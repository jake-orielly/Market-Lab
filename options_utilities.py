import yfinance as yf
from pandas import DataFrame
from math import sqrt
from datetime import date

def get_option_chain(ticker,date,contractType):
    if contractType == 'call':
        contractType = 0
    elif contractType == 'put':
        contractType = 1
    else:
        raise Exception('Bad contract type', contractType)
    chain = ticker.option_chain(date)[contractType]
    return chain

def options_metrics():
    return ['strike','lastPrice','breakEven','percentReturn','percentOfCurr','breakEvenPercentDiff','impliedVolatility','sdMove','sdToBreakEven']

def get_within_percent(tickerName,date,percent,contractType):
    ticker = yf.Ticker(tickerName)
    option_df = get_option_chain(ticker,date,contractType)
    curr_price = get_curr_price(tickerName)
    add_percent(option_df,curr_price)
    add_break_even(option_df,contractType)
    add_percent_return(option_df)
    add_break_even_percent_diff(option_df,curr_price)
    add_sd_move(option_df,curr_price,date)
    add_sds_to_break_even(option_df,curr_price)
    max_strike = curr_price + curr_price * percent/100
    min_strike = curr_price - curr_price * percent/100
    matching = option_df.loc[(option_df['strike'] >= min_strike) & (option_df['strike'] <= max_strike),options_metrics()]
    return  matching.sort_values(by='lastPrice', ascending=True)

def get_curr_price(tickerName):
    ticker = yf.Ticker(tickerName)
    curr_price = ticker.history('1d')['Close'][0]
    return curr_price

# Adds percent of current price as column
def add_percent(df,curr_price):
    percent = []
    for i in range(len(df)):
        percent.append((df['strike'][i]/curr_price))
    df['percentOfCurr'] = percent 

def add_break_even(df,contractType):
    break_even = []
    if (contractType == 'put'):
        price_mod = -1
    else:
        price_mod = 1
    for i in range(len(df)):
        break_even.append(df['strike'][i] + df['lastPrice'][i] * price_mod)
    df['breakEven'] = break_even 

def add_percent_return(df):
    percent_return = []
    for i in range(len(df)):
        val = df['lastPrice'][i] / (df['strike'][i] - df['lastPrice'][i])
        percent_return.append(val)
    df['percentReturn'] = percent_return 

def add_break_even_percent_diff(df,curr_price):
    percent = []
    for i in range(len(df)):
        percent.append((df['breakEven'][i] - curr_price) / curr_price * 100)
    df['breakEvenPercentDiff'] = percent 

def add_sd_move(df,curr_price,expiration):
    percent = []
    days_to_expr = days_from_today(expiration)
    for i in range(len(df)):
        val = curr_price * df['impliedVolatility'][i] * sqrt(days_to_expr) / sqrt(365)
        percent.append(val)
    df['sdMove'] = percent 

def add_sds_to_break_even(df,curr_price):
    sd_to_break_even = []
    for i in range(len(df)):
        val = abs(curr_price - df['breakEven'][i]) / df['sdMove'][i]
        sd_to_break_even.append(val)
    df['sdToBreakEven'] = sd_to_break_even 

def days_from_today(exp_date):
    e_year,e_month,e_day = [int(i) for i in exp_date.split('-')]
    expiration = date(e_year,e_month,e_day)
    today = date.today()
    return (expiration - today).days + 1
    

def get_option_dates(ticker):
    return ticker.options