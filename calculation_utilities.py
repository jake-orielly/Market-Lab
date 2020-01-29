import yfinance as yf

def add_percent_change(df):
    change = []
    change.append(0)
    for i in range(1,len(df)):
        change.append((df['Close'][i] - df['Close'][i-1]) / df['Close'][i-1] * 100)
    df['Change'] = change 