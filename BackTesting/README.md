# BackTesting

## Description
The Backtesting engine developed by us, takes in input the log file, and gives detailed metrics to evaluate the strategy used to generate the logs
There are two files `run_engine.py` and `main_engine.py`\
`main_engine.py` contains the class and functions, to run the engine, and `run_engine.py` is a wrapper to call the backtester with static or compounding approach of trading

1. Static approach : Each trade executed is of 1000$
2. Compounding approach : We start with 1000$ cash, and reinvest the total cash (Initial cash + PnL generated) we have whenever entering the trade


## Usage
1. Install the required dependencies: `pip install -r requirements.txt`
2. Run the application: `python3 run_engine.py --data 'path of data file' --method 'static/compounding/both'`
3. Observe the results and the plot

## Metrics

The backtesting engine generates the following metrics:

- **Net PnL**: The net profit or loss.
- **Buy and Hold PnL**: The profit or loss if the asset was held from the start to the end of the period.
- **Total Trades Closed**: The total number of trades that were closed.
- **Gross Profit**: The total profit from winning trades.
- **Gross Loss**: The total loss from losing trades.
- **Largest Winning Trade**: The largest profit from a single trade.
- **Largest Losing Trade**: The largest loss from a single trade.
- **Min Net PnL**: The lowest net profit or loss.
- **Sharpe Ratio**: The risk-adjusted return of the strategy.
- **Average Winning Trade**: The average profit from winning trades.
- **Average Losing Trade**: The average loss from losing trades.
- **Number of Winning Trades**: The total number of winning trades.
- **Number of Losing Trades**: The total number of losing trades.
- **Total Transaction Cost**: The total cost of all trades.
- **Maximum Drawdown**: The largest drop in value from a peak to a trough.
- **Maximum Trade Holding Duration**: The longest time a single trade was held.
- **Average Trade Holding Duration**: The average time a trade was held.
- **Annual Returns**: The annualized return of the strategy.
- **Annual Maximum Drawdowns**: The largest annual drop in value from a peak to a trough.