## Steps to Run

I have stored all the analysis in the notebook attached. To run you would first need to install all the libraries in your condo environment mentioned in requirements.txt

This strategy trades on open price, both long/short. The signals were generated on 1d tick, with finer stop loss on 1h tick.

`conda install --file requirements.txt`

The bitcoin data is in the data-folder
To just generate the logs, you can just run the last 2 cells

Logs file

macd_train.csv: Train set
macd_val: Val set
macd_comb.csv: Train + Val
macd_comb_final.csv: Train + Val + Test