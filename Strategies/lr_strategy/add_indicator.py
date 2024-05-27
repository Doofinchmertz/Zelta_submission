from Utils import *
import argparse
import warnings
from Optimal_constants import *

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument("--data", help="Location for OHLCV data", required=True)
args = parser.parse_args()

# Load data
df = get_data("../../data/"+args.data)


# Remove any row with zero volume
df = df[df['volume']!=0]


# INDICATOR 1: Daily Return - Percentage change in close price"
df['Daily_Return'] = df['close'].pct_change()*1000


# INDICATOR 2: Adding RSI: RSI is scaled between -50 and 50, and values between -20 and 20 are set to 0
df['RSI'] = list(get_processed_RSI(df, period=OPTIMAL_PERIOD_FOR_RSI))


# INDICATOR 3: Adding exp_RSI: exp_RSI has the magnitude of exp of absolute RSI, and sign inverse of RSI, it has also been scaled
df['exp_RSI'] = list(get_exp_RSI(df))


# INDICATOR 4: Adding MFI: money_flow_index
df['MFI'] = list(money_flow_index(df, OPTIMAL_PERIOD_FOR_MFI))


# INDICATOR 5: Adding EMA_Slope: EMA is exponential moving average, we have the slope of this as an indicator
df['EMA_Slope'] = get_ema_slope(df, period=OPTIMAL_PERIOD_FOR_EMA)


# Drop columns macd, signal, EMA, high, low
df = df.drop(['EMA', 'high', 'low'], axis=1)

# Drop rows with any Nan value
df = df.dropna()

# Get the final df with indicators and save it in data_with_indicators folder
df.to_csv("data_with_indicators/" + args.data[:-4] + "_with_indicators.csv")