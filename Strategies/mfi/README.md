# Money Flow Index

This folder contains the implementation of the `Money Flow Index`, a trading strategy based on money flow in the market, for 1h tick size. This strategy trades on close, both long/short

## Files



- **mfi.py**: This script applies mfi strategy to the data file. It takes one argument, `data`, which is the name of the file. The data file should be located in the `data` folder in the main directory.

```
python mfi.py --data data_file.csv
```

- **utils.py**: It is typically used to store utility functions or helper functions that are used across multiple scripts or modules within a project. The utility functions used here are -
  
  * money_flow_index: This function calculates the money flow of the market
  * plots_candlestick: This function generates a candlestick chart with additional indicators and volume bars based on the provided data. It saves the chart as a PNG image and an HTML file.

  * clear_folders: This function clears the contents of the "plots" and "htmls" folders by deleting all the files inside them.


- **Optimal_constants.py**: This file contains optimal constants used thoughout the directory. These constants have been set after rigorous testing on the initial 60 percent of the data to get the best performance metrics possible.

## Usage

To use this strategy, follow these steps:

1. Make sure you setup your environment using the `requirements.txt` file in this directory.
2. Place the data file in the `data` folder in the main directory. (ex - data_file.csv)
3. Run the `mfi.py` script, passing the name of the data file as the argument. (An example command has been shown above)

## Logs
Logs for this strategy can be found in the `logs` folder of this directory.