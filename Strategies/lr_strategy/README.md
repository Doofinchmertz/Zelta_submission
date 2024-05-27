# LR_Strategy

This folder contains the implementation of the `lr_strategy`, a trading strategy based on linear regression, for 1hr tick size. This strategy trades on closing prices, both long/short

## Files

- **add_indicator.py**: This script adds technical indicators to the given data file. It takes one argument, `data`, which is the name of the file. The data file should be located in the `data` folder in the main directory.

```
python add_indicator.py --data data_file.csv
```

- **linear_model.py**: This script applies a linear regression model to the data file. It also takes one argument, `data`, which is the name of the file. The data file with the added indicators is already stored in the `data_with_indicators` folder in this directory. 

```
python linear_model.py --data data_file.csv
```

- **Utils.py**: It is typically used to store utility functions or helper functions that are used across multiple scripts or modules within a project. The utility functions used here are -
* get_data(filename) - Wrapper function for read_file, reads a CSV file and returns a DataFrame with the data.
* read_file(filename) - Reads a CSV file and returns a DataFrame with the data.
* def money_flow_index(data, period=14) - Calculates the Money Flow Index (MFI) for the given data over a specified period.
* pnl(df) - Calculates the profit and loss (PnL) for a series of trades represented in a DataFrame.
* stop_loss(data, thresh) - Implements a stop loss strategy on the trading data, exiting trades when losses exceed a specified threshold.
* get_processed_RSI(df, period=80) - Calculates the Relative Strength Index (RSI) for the given data over a specified period and applies some additional processing.
* get_exp_RSI(rsi) - Applies an exponential transformation to the RSI values and scales the result.
* get_ema_slope(df, period=2) - Calculates the slope of the Exponential Moving Average (EMA) for the given data over a specified period and scales the result.


- **Optimal_constants.py**: This file contains optimal constants used thoughout the directory. These constants have been set after rigorous testing to get the best performance metrics possible.

## Usage

To use this strategy, follow these steps:

1. Make sure you setup your environment using the `requirements.txt` file in this directory.
2. Place the data file in the `data` folder in the main directory. (ex - data_file.csv)
3. Run the `add_indicator.py` script, passing the name of the data file as the argument. (An example command has been shown above)
4. Run the `linear_model.py` script, passing the name of the data file as the argument. (An example command has been shown above)

## Logs
Logs for this strategy can be found in the `logs` folder of this directory.