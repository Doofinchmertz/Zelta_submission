# Median_Reversion

This directory hosts the code for the `median_reversion` strategy. This trading approach is premised on the belief that, over time, asset prices tend to gravitate back towards their median value. This strategy trades on close, both long/short

## Files



- **median_reversion.py**: This script applies median reversion strategy to the data file of 3m tick size. It takes one argument, `data`, which is the name of the file. The data file should be located in the `data` folder in the main directory.

```
python median_reversion.py --data data_file.csv
```

- **Optimal_constants.py**: This file contains optimal constants used thoughout the directory. These constants have been set after rigorous testing to get the best performance metrics possible.

## Usage

To use this strategy, follow these steps:

1. Make sure you setup your environment using the `requirements.txt` file in this directory.
2. Place the data file in the `data` folder in the main directory. (ex - data_file.csv)
3. Run the `median_strategy.py` script, passing the name of the data file as the argument. (An example command has been shown above)

## Logs
Logs for this strategy can be found in the `logs` folder of this directory.