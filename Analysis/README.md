


## Data Analysis 

In this project we have tried to explore the different patterns and inference which can be drawn from the data


## Indicators 

In this project we have tested and developed various technical indicators for the purpose of selecting the best ones
suited as per required strategies

## Trade Visualization Tool

The folder contains script for analyzing trades with better visualization. One usecase is demonstrated in html and plots folder

## Misc_analysis 

The folder contains jupyter notebook for other important experimentation performed technical indicators based on mathematical analysis and insights drawn from data

## Correlation Analysis
This folder contains python notebook for detailed correlation analysis between various important features that are been used in various strategies

## Rolling Lr Analysis
This folder contains thre jupyter notebooks which were used to draw statistical inferences about the features used for the model and the hyperparameters used

## stoploss_polt.py

Function takes as input that contains column 'logs', that contain the buy/sell singals (in 1, -1 format)

This function also assumes that we trade on the open; to trade at the close, please change the open column to close in the function

The plotting lines are to plot the final returns of the trades against the lowest returns (while the trade was opened)