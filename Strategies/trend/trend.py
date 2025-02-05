import pandas as pd
import numpy as np
import sys
import warnings
import argparse
from utils import *
from optimum_param import *
warnings.filterwarnings('ignore')

parser = argparse.ArgumentParser(description="Trend Strategy")
parser.add_argument("--data", type = str,  help = "Path to data file", required = True)
args = parser.parse_args()
df = pd.read_csv('../../data/'+args.data)
df = df.reset_index(drop=True)

def apply_trading_strategy(df, flag_column, log_column, stop_loss_thresh=-0.07):
    """Apply trading strategy based on trend Bands."""
    exit_loss = 0
    compare = 0
    df[log_column] = np.nan

    for i in range(len(df)):
        if df[flag_column].iloc[i] == 1 and compare == 0:
            exit_loss = 0
            buy_price = df["close"].iloc[i]
            compare = 1
            df[log_column].iloc[i] = 1
        elif (df[flag_column].iloc[i] != -1 and compare == 1):
            df[log_column].iloc[i] = 0
            sell_price = df["close"].iloc[i]
            exit_loss = (sell_price - buy_price) / buy_price
            if exit_loss < stop_loss_thresh:
                df[log_column].iloc[i] = -1
                compare = 0
        elif df[flag_column].iloc[i] == -1 and compare == 1:
            df[log_column].iloc[i] = -1
            compare = 0
        elif df[flag_column].iloc[i] == -1 and compare == 0:
            exit_loss = 0
            sell_price = df["close"].iloc[i]
            compare = -1
            df[log_column].iloc[i] = -1
        elif (df[flag_column].iloc[i] != 1 and compare == -1):
            df[log_column].iloc[i] = 0
            buy_price = df["close"].iloc[i]
            exit_loss = (sell_price - buy_price) / sell_price
            if exit_loss < stop_loss_thresh:
                df[log_column].iloc[i] = 1
                compare = 0
        elif df[flag_column].iloc[i] == 1 and compare == -1:
            df[log_column].iloc[i] = 1
            compare = 0
        elif df[flag_column].iloc[i] == 0 and compare == 0:
            df[log_column].iloc[i] = 0

    df[log_column].fillna(0, inplace=True)
    df[log_column].iloc[-1] = -np.sum(df[log_column])
    return df

# Calculate Bollinger Bands
df = calculate_trend(df, length, mult)

# Determine Indicator
df = determine_indicator(df)

# Apply Trading Strategy
df = apply_trading_strategy(df, flag_column='indicator', log_column='signals')

# Save to CSV
df.to_csv(".\logs\logs_trend.csv")