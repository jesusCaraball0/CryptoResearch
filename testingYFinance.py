
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
