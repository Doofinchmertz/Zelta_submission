## Indicators 
In this project we have tested and developed various custom technical indicators and their optimal parameter for the purpose of selecting the best ones
suited as per required strategies

# Importing Relevant Libraries
The script starts by importing necessary Python libraries for data handling (Pandas, Numpy), statistical analysis (Scipy, Statsmodels), visualization (Seaborn, Matplotlib), and machine learning (Scikit-learn)

# Data Preparation
Loads Bitcoin trading data from CSV files for different timeframes (3m, 5m, 15m, 30m, 1h).
Renames columns, converts date strings to datetime objects, and sets date as the index.
Drops unnecessary columns and calculates return values and absolute return values for various periods.

# Key Features 

Volume Weighted Average Price (VWAP): Computes VWAP for 5-minute intervals.

Price Spread Analysis: Examines the open-close price spread and its absolute values.

Correlation Analysis: Assesses the relationships between different market indicators.

Relative Strength Index (RSI) Optimization: Finds optimal RSI parameters for trading signals.

Directional Movement Indicators (DMI): Utilizes PLUS_DM and MINUS_DM to generate trading signals.

Moving Averages: Analyzes Simple Moving Average (SMA), Exponential Moving Average (EMA), Triple EMA (TEMA), and Weighted Moving Average (WMA) for trend analysis and signal generation.

Conclusion
We have developed various custom indicators and found its optimal parameters to maximize correlation with future returns, these would help in developing trading strategies




