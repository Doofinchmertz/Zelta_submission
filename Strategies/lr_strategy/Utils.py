import numpy as np
import pandas as pd
import talib
from sklearn.preprocessing import StandardScaler

def money_flow_index(data, period=14):
    # Calculate typical price
    typical_price = (data['high'] + data['low'] + data['close']) / 3

    # Calculate raw money flow
    raw_money_flow = typical_price * data['volume']

    # Get the direction of the money flow
    money_flow_direction = [1 if typical_price[i] > typical_price[i - 1] else (-1 if typical_price[i] < typical_price[i - 1] else 0) for i in range(1, len(typical_price))]

    # Pad the money flow direction with 0 for the first element
    money_flow_direction.insert(0, 0)

    # Calculate positive and negative money flow
    positive_money_flow = [0 if direction == -1 else raw_money_flow[i] for i, direction in enumerate(money_flow_direction)]
    negative_money_flow = [0 if direction == 1 else raw_money_flow[i] for i, direction in enumerate(money_flow_direction)]

    # Calculate 14-day sums of positive and negative money flow
    positive_money_flow_sum = pd.Series(positive_money_flow).rolling(window=period, min_periods=1).sum()
    negative_money_flow_sum = pd.Series(negative_money_flow).rolling(window=period, min_periods=1).sum()

    # Calculate money flow index
    money_flow_ratio = positive_money_flow_sum / negative_money_flow_sum
    money_flow_index = 100 - (100 / (1 + money_flow_ratio))

    return money_flow_index

def pnl(df):

    df_trades= df[df["signals"] != 0].reset_index(drop = True)
    returns = []

    signs = []

    for i in range(0, len(df_trades), 2):

        entry_price = df_trades["close"].iloc[i]
        exit_price = df_trades["close"].iloc[i+1]
    

        sign = df_trades["signals"].iloc[i]

        returns.append(((exit_price-entry_price)/entry_price*sign - 0.15/100)*1000)
        signs.append(sign)

    return np.sum(returns)

def stop_loss(data, thresh):

    exit_loss = 0
    disable_trading = 0
    compare = 0
    thresh = -thresh
    logs = []
    for i in range(len(data)):
        if data["flag"].iloc[i] == 1 and compare == 0:
            # No open trade, encouter buy singal
            exit_loss = 0
            buy_price = data["close"].iloc[i]
            
            compare = 1
            logs.append(1)

        #Once we close a trade, we have to check in df_fine whether to exit or not

        elif (data["flag"].iloc[i] != -1 and compare == 1):
            # Current buy trade, encounter buy signal or no signal - do nothing, update stop loss
            logs.append(0)

            #calculate pnl, if we exit now
            sell_price = data["close"].iloc[i]
            exit_loss = (sell_price - buy_price)/buy_price 
            

            #exit trade, if the loss is higher than stop loss
            if exit_loss < thresh and disable_trading == 0:
                logs[-1] = -1
                disable_trading = 1


        elif data["flag"].iloc[i] == -1 and compare == 1:
            # Current buy trade, encounter sell signal

            #exit trade
            logs.append(-1)
            compare = 0
            exit_loss = 0

            #if trade was already exited before, check for disable trading flag here, do nothing here
            if disable_trading == 1:
                disable_trading = 0
                logs[-1] = 0


        #SHORT TRADES
        elif data["flag"].iloc[i] == -1 and compare == 0:
            # No open trade, enounter sell siganl 
            exit_loss = 0
            sell_price = data["close"].iloc[i]
            
            compare = -1
            logs.append(-1)


        elif (data["flag"].iloc[i] != 1 and compare == -1):
            # Current sell trade, encounter sell signal or no signal - do nothing, update stop loss
            logs.append(0)

            #calculate pnl, if we exit now
            buy_price = data["close"].iloc[i]
            exit_loss = (sell_price - buy_price)/sell_price 
        

            #exit trade, if the loss is higher than stop loss
            if exit_loss < thresh and disable_trading == 0:
                logs[-1] = 1
                disable_trading = 1

        elif data["flag"].iloc[i] == 1 and compare == -1:

            #exit trade
            logs.append(1)
            compare = 0
            exit_loss = 0

            #if trade was already exited before, check for disable trading flag here, do nothing here
            if disable_trading == 1:
                disable_trading = 0
                logs[-1] = 0

        elif data["flag"].iloc[i] == 0 and compare == 0:
            logs.append(0)

    #close out positions (if needed)
    logs[-1] = -np.sum(logs[:-1])

    data["logs"] = np.array(logs)

    # rename column logs to signal
    data.rename(columns={'logs': 'signals'}, inplace=True)

    return data

def read_file(filename):
    return pd.read_csv(filename, index_col=0, parse_dates=True, infer_datetime_format=True)

def get_data(filename):
    return read_file(filename)

def get_processed_RSI(df, period=80):
    rsi = talib.RSI(df['close'], timeperiod=period)
    rsi -= 50
    rsi = rsi.apply(lambda x: x if x > 20 or x < -20 else 0)
    rsi = rsi.apply(lambda x: x - 20 if x >= 20 else x)
    rsi = rsi.apply(lambda x: x + 20 if x <= -20 else x)    
    rsi.fillna(0,inplace=True)
    return rsi

def get_exp_RSI(df):
    df['exp_RSI'] = np.exp(np.abs(df['RSI']))
    df['exp_RSI'] = np.where(df['RSI'] > 0, -df['exp_RSI'], df['exp_RSI'])

    # Scale exp_RSI
    scaler1 = StandardScaler()
    df['exp_RSI'] = scaler1.fit_transform(df['exp_RSI'].values.reshape(-1,1))

    return df['exp_RSI']

def get_ema_slope(df, period=2):
    df['EMA'] = talib.EMA(df['close'], timeperiod=2)
    df['EMA_slope'] = -df['EMA'].pct_change(1)*100
    df.fillna(0, inplace=True)

    # Scale EMA_Slope
    scaler2 = StandardScaler()
    df['EMA_slope'] = scaler2.fit_transform(df['EMA_slope'].values.reshape(-1, 1))

    return df['EMA_slope']
