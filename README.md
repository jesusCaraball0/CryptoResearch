# Crypto Strategy Backtesting
## Description
Python script that tests the 5 most popular stock chart patterns, as detailed by Prof. Robert Levy in 1971, on the 5 most popular cryptocurrencies. The backtest engine in this script collects historical price data totalling to over 900,000 rows and records how many times each pattern showed up and out of those, how often it was accurate. 

It uses NumPy for fast numeric comparisons, Pandas for convenient time series data storage, and the yFinance API to access historical prices from Yahoo Finance.  

## Install Instructions
The script runs locally. After forking the repo and downloading the source file, install necessary dependencies through either a virtual or conda environment. These are NumPy, Pandas, and yFinance. Also, change the time frame to be within the past 60 days (this is a limination of yFinance).

## Future Contribution Ideas
1. Create a web scraping app to retrieve data from Yahoo Finance directly (their TOS allows this).
2. Create an app to export results in csv format, rather than print on the terminal.
3. Update backtesting engine to test more complex technical strategies. 
