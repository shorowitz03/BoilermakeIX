import sys
import numpy as np
import pandas as pd
import yfinance as yf

stocks = open('garrett\\tickers.txt', 'r').readline().split(',')[1:-1]
print(stocks)

incTickers, excTickers= [], []

#data = yf.download(tickers=stocks[0], start='2020-01-01', interval='1d', progress=False)
for s in stocks:
    try:
        data = yf.download(tickers=s, period='2m', interval='1m', progress=False)
        incTickers.append(s)
    except:
        excTickers.append(s)

'''
fileName = 'stockData/' + stocks[0] + '.txt'
sys.stdout = open(fileName, 'w')
print(data.to_csv(index=True, line_terminator='\n'))
'''