
# raw packages
import pandas as pd
import numpy as np

# Data Source

import yfinance as yf

# Data Visualization

import finplot as fplt


Bitcoin = yf.Ticker("BTC-USD")
Ethereum = yf.Ticker("ETH-USD")
Binance = yf.Ticker("BNB-USD")
Solana = yf.Ticker("SOL-USD")
Lido = yf.Ticker("STETH-USD")

def priceChart(priceHistory):

    fplt.candlestick_ochl(priceHistory[['Open','Close','High','Low']])
    fplt.show()

    return 0


def main():
                                                                                                                                                                                                                                                                                                                                                                        
    #prints Bitcoin, Ethereum, and Binance price history data for january and february
    START = '2024-08-5'
    END = '2024-10-02'

    btcHist = Bitcoin.history(start = START, end=END, interval='15m')
    ethHist = Ethereum.history(start = START, end=END, interval='15m')
    bnbHist = Binance.history(start = START, end=END, interval='15m')
    solHist = Solana.history(start = START, end=END, interval='15m')
    lidHist = Lido.history(start=START, end=END, interval='15m')

 

    for i in range(1,6):
        TestPattern1(btcHist.iloc[:,0].tolist(), "Bitcoin", i)
        TestPattern1(ethHist.iloc[:,0].tolist(), "Ethereum", i)
        TestPattern1(bnbHist.iloc[:,0].tolist(), "Binance", i)
        TestPattern1(solHist.iloc[:,0].tolist(), "Solana", i)
        TestPattern1(lidHist.iloc[:,0].tolist(), "Lido Staked", i)


    return 0


def TestPattern1(pricesList, crypto, patternNumber):
    patternRec = 0 # number of times pattern appeared
    patternCor = 0 #number of times pattern worked

    percentGains = [] #list of the percent gains to be made from winning trades
    percentLosses = [] #list of the percent losses to be made from losing trades



    for i in range(6, len(pricesList)): #Counts how many times pattern appeared / worked across 2 months
          if patternNumber == 1:
                condition = pricesList[i-1] < pricesList[i-3] < pricesList[i-2] < pricesList[i-5] > pricesList[i-4]
          elif patternNumber == 2:
                condition = pricesList[i-1] < pricesList[i-3] < pricesList[i-5] < pricesList[i-2] > pricesList[i-4]
          elif patternNumber == 3:
                condition = pricesList[i-1] < pricesList[i-5] < pricesList[i-3] < pricesList[i-2] > pricesList[i-4]
          elif patternNumber == 4:
                condition = pricesList[i-1] < pricesList[i-3] < pricesList[i-5] < pricesList[i-4] > pricesList[i-2]
          elif patternNumber == 5:
                condition = pricesList[i-1] < pricesList[i-5] < pricesList[i-3] < pricesList[i-4] > pricesList[i-2]
          if condition:
               patternRec += 1
               if pricesList[i] < pricesList[i-1]:
                     patternCor += 1
                     percentGains.append((pricesList[i-1] - pricesList[i])/pricesList[i])
               else:
                     percentLosses.append((pricesList[i-1] - pricesList[i]) / pricesList[i])


    sum = 0
    for i in range(len(percentGains)):
        sum += percentGains[i]

    sumLoss = 0
    for i in range(len(percentLosses)):
        sumLoss += percentLosses[i]

    print(f"The results for pattern {patternNumber} tested on {crypto} are:")
    documentResults(patternRec, patternCor, sum, sumLoss, (pricesList[len(pricesList) - 1] - pricesList[0]) / pricesList[0])
    return 0


def documentResults(patternRec, patternCor, sumGains, sumLoss, bhReturns):
    print(f"Number of times the pattern was recognized: {patternRec}")
    print(f"Number of times the pattern was correct: {patternCor}")
    print(f"for winning trades, the total percentage gain was: {sumGains * 100}")
    print(f"for losing trades, the total percentage lost was: {sumLoss * 100}")
    print(f"The total aggregate returns for the strategy was: {(sumGains + sumLoss) * 100}")
    print(f"Comparably, a the returns for a buy and hold strategy during the same period was: {bhReturns * 100}")
    print()



if __name__ == "__main__":
    main()

# # Import necessary libraries
# import finplot as fplt
# import pandas as pd

# # Import necessary libraries
# import yfinance as yf
# import pandas as pd
# from datetime import datetime, timedelta

# # Define the end date as today and the start date as 2 years ago
# end_date = datetime.today().strftime('%Y-%m-%d')
# start_date = (datetime.today() - timedelta(days=730)).strftime('%Y-%m-%d')

# # Retrieve Bitcoin data
# bitcoin_data = yf.download('BTC-USD', start=start_date, end=end_date)

# # Retrieve Ethereum data
# ethereum_data = yf.download('ETH-USD', start=start_date, end=end_date)

# # Reset index to include date as a column
# bitcoin_data.reset_index(inplace=True)
# ethereum_data.reset_index(inplace=True)

# # Rename columns for clarity
# bitcoin_data = bitcoin_data.rename(columns={'Open': 'Bitcoin_Open', 'High': 'Bitcoin_High', 'Low': 'Bitcoin_Low', 'Close': 'Bitcoin_Close', 'Adj Close': 'Bitcoin_Adj_Close', 'Volume': 'Bitcoin_Volume'})
# ethereum_data = ethereum_data.rename(columns={'Open': 'Ethereum_Open', 'High': 'Ethereum_High', 'Low': 'Ethereum_Low', 'Close': 'Ethereum_Close', 'Adj Close': 'Ethereum_Adj_Close', 'Volume': 'Ethereum_Volume'})

# # Merge Bitcoin and Ethereum data
# data = pd.merge(bitcoin_data, ethereum_data, on='Date', suffixes=('_bitcoin', '_ethereum'))

# # Select relevant columns
# data = data[['Date', 'Bitcoin_High', 'Bitcoin_Low', 'Ethereum_High', 'Ethereum_Low']]


# # Define a function to plot the data
# def plot_data(data):
#     # Separate Bitcoin and Ethereum data
#     bitcoin_data = data[['Date', 'Bitcoin_Open', 'Bitcoin_High', 'Bitcoin_Low', 'Bitcoin_Close', 'Bitcoin_Volume']]
#     ethereum_data = data[['Date', 'Ethereum_Open', 'Ethereum_High', 'Ethereum_Low', 'Ethereum_Close', 'Ethereum_Volume']]

#     # Rename columns for finplot
#     bitcoin_data = bitcoin_data.rename(columns={'Date': 'time', 'Bitcoin_Open': 'open', 'Bitcoin_High': 'high', 'Bitcoin_Low': 'low', 'Bitcoin_Close': 'close', 'Bitcoin_Volume': 'volume'})
#     ethereum_data = ethereum_data.rename(columns={'Date': 'time', 'Ethereum_Open': 'open', 'Ethereum_High': 'high', 'Ethereum_Low': 'low', 'Ethereum_Close': 'close', 'Ethereum_Volume': 'volume'})

#     # Set time as index
#     bitcoin_data.set_index('time', inplace=True)
#     ethereum_data.set_index('time', inplace=True)

#     # Plot Bitcoin data
#     ax, axv = fplt.create_plot('Bitcoin', rows=2)
#     fplt.candlestick_ochl(bitcoin_data[['open', 'close', 'high', 'low']])
#     fplt.volume_ocv(bitcoin_data[['open', 'close', 'volume']], colorfunc=fplt.strength_colorfilter)
#     fplt.show()

#     # Plot Ethereum data
#     ax, axv = fplt.create_plot('Ethereum', rows=2)
#     fplt.candlestick_ochl(ethereum_data[['open', 'close', 'high', 'low']])
#     fplt.volume_ocv(ethereum_data[['open', 'close', 'volume']], colorfunc=fplt.strength_colorfilter)
#     fplt.show()

# # Call the function with the data
# plot_data(data)