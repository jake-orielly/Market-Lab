import yfinance as yf

def add_percent_change(df):
    change = []
    change.append(0)
    for i in range(1,len(df)):
        change.append((df['Close'][i] - df['Close'][i-1]) / df['Close'][i-1] * 100)
    df['Change'] = change 

def calculate_rsi(history):
    gains = []
    losses = []
    prev = None
    for row in history:
        if prev == None:
            prev = row
        else:
            diff = row/prev - 1
            if diff > 0:
                gains.append(diff * 100)
            elif diff < 0:
                losses.append(abs(diff * 100))
            prev = row
    avg_gain = sum(gains)/len(history)
    avg_loss = sum(losses)/len(history)

    avg_gain = avg_gain if avg_gain != 0 else 1
    avg_loss = avg_loss if avg_loss != 0 else 1
    rsi = 100 - (100/(1 + avg_gain/avg_loss))
    return rsi

def add_rsi(history,rsi_periods):
    rsi_history = [None]
    for i in range(len(history[1:])):
        if (i >= rsi_periods):
            curr_rsi = calculate_rsi(history['Close'][i+1-rsi_periods:i+1])
        else:
            curr_rsi = calculate_rsi(history['Close'][0:i+1])
        rsi_history.append(curr_rsi)
    history['RSI'] = rsi_history

#ticker = yf.Ticker('TSLA')
#history = ticker.history('3mo')
#add_rsi_to_history(history,14)
#print(history)