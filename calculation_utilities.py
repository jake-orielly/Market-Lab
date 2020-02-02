import yfinance as yf

def add_percent_change(df):
    change = []
    change.append(0)
    for i in range(1,len(df)):
        change.append((df['Close'][i] - df['Close'][i-1]) / df['Close'][i-1] * 100)
    df['Change'] = change 

def calculate_rsi(ticker):
    history = yf.Ticker(ticker).history('15d')
    gains = []
    losses = []
    prev = None
    for _, row in history.iterrows():
        if prev == None:
            prev = row['Close']
        else:
            diff = row['Close']/prev - 1
            if diff > 0:
                gains.append(diff * 100)
            elif diff < 0:
                losses.append(abs(diff * 100))
            prev = row['Close']
    avg_gain = sum(gains)/14
    avg_loss = sum(losses)/14

    rsi = 100 - (100/(1 + avg_gain/avg_loss))
    return rsi

print(calculate_rsi('AAPL'))
print(calculate_rsi('MSFT'))
print(calculate_rsi('F'))