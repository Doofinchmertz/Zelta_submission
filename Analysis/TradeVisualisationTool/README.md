# Trade Analyser

This script contains functions for analyzing trades. 

## Overview

The `trade_analyser.py` script includes the following functions:

## Function: plot_trade

The plot_trade function is used to visualize a trade on a price chart.

### Arguments

- `df`: A pandas DataFrame containing the data to be plotted. The DataFrame should have columns for 'datetime', 'open', 'high', 'low', and 'close'.

- `entry_idx`: The index in the DataFrame of the entry point for the trade. This is used to select the subset of data to be plotted.

- `exit_idx`: The index in the DataFrame of the exit point for the trade. This is used to select the subset of data to be plotted.

- `trade_type`: Type of trade: long/short
- `title`: Title given to the plot may include time stamp of entry, reason of entry and exit etc.

- `lookback`: The number of rows before and after the entry and exit points to include in the subset of data to be plotted. Defaults to 20.

### Example
One usecase Shown in the htmls and plots folder. 