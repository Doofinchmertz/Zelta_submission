## Indicators 
In this project we have tested and developed various technical indicators for the purpose of selecting the best ones
suited as per required strategies

# Importing Relevant Libraries
The script starts by importing necessary Python libraries for data handling (Pandas, Numpy), statistical analysis (Scipy, Statsmodels), visualization (Seaborn, Matplotlib), and machine learning (Scikit-learn)

# Data Preparation
Loads Bitcoin trading data from CSV files for different timeframes (3m, 5m, 15m, 30m, 1h).
Renames columns, converts date strings to datetime objects, and sets date as the index.
Drops unnecessary columns and calculates return values and absolute return values for various periods.
# Indicators 

## Major Indicators
A comprehensive list of 15 different technical indicators (momentum oscillators,volume,volatility) is provided. Each one is followed by a Python function to calculate the respective indicator on the provided data frames. Examples include the Relative Strength Index (RSI), Stochastic Oscillator, and Commodity Channel Index (CCI).

Code for Candlestick pattern identifiers have been added if the strategy requires any particular candlestick support.

## Correlation Calculation
A function calculate_correlation is defined to calculate Pearson, Spearman and Kendall correlations between signal and return columns of the data frame.
We are checking the indicators' with correlation with future returns_2 (close(t+2)/close(t)) and returns(close(t+1)/close(t)) and their absolute values
For identifying the indicators which have the most potential in predicting future returns along with their direction

## Implementation of TA-Lib Indicators
This section involves using the TA-Lib library to calculate various technical indicators. Indicators are applied on different timeframes of Bitcoin data (like 5m, 15m, 30m, 1h). This includes volume indicators, momentum indicators, and pattern recognition functions.


## Alpha Based Indicators
Custom alpha indicators are developed and tested for their effectiveness using correlation coefficients and Information Coefficient (IC). These indicators are based on different mathematical and statistical formulations and are tested across various timeframes.

# Conclusion
In this report we have tested 30+ indicators and analyzed their performance and performed indicator sensitivity analysis across different tick sizes. The results are reported in indicators.xlsx

