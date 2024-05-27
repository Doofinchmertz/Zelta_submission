import numpy as np
import argparse
from Utils import *
import warnings
from Optimal_constants import *
import pickle

warnings.filterwarnings("ignore")

parser = argparse.ArgumentParser()
parser.add_argument("--data", help="Location for data_with_indicators", required=True)


# read the arguments and store it in a variable
args = parser.parse_args()
thresh = STOPLOSS_THRESHOLD

# Load data
df = get_data("data_with_indicators/"+ args.data[:-4] + "_with_indicators.csv")

# Define the independent variables
X = df[['volume', 'Daily_Return', 'RSI', 'exp_RSI', 'MFI', 'EMA_Slope']]

# Load the linear regression model using statsmodels
model = pickle.load(open("model.pkl", 'rb'))

# Initialize flag column with 0
df['flag'] = 0

# Predict the dependent variable of the training data
y_pred = model.predict(X)

# Get the quantile values for the positive and negative predictions
positive_quantile = float(OPTIMAL_POSITIVE_QUANTILE)/100
positive_quantile_value = np.quantile(np.abs(y_pred), positive_quantile)
negative_quantile = float(OPTIMAL_NEGATIVE_QUANTILE)/100
negative_quantile_value = -np.quantile(np.abs(y_pred), negative_quantile)

# Trading strategy: Buy if y_pred > positive_quantile_value, Sell if y_pred < negative_quantile_value, Hold otherwise
df['flag'] = np.where(y_pred > positive_quantile_value, 1, np.where(y_pred < negative_quantile_value, -1, 0))

# Implement stop loss and get the logs
df = stop_loss(df, thresh)

# Save the logs in the logs folder
df.to_csv("logs/" + args.data)