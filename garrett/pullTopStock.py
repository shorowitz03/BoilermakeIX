import sys
import numpy as np
import pandas as pd
import yfinance as yf

stocks = ['UBER']
stocks = [x.split(',')[0].strip(' ', '') for x in open('garrett\\nasdaq_screener_1642839777222.txt', 'r')]
sys.stdout = open('tickers.txt', 'w')
for x in stocks:
    print(x, end=',')



'''
data = yf.download(tickers=stocks[0], start='2020-01-01', interval='1d', progress=False)

fileName = 'stockData/' + stocks[0] + '.txt'
sys.stdout = open(fileName, 'w')

print(data.to_csv(index=True, line_terminator='\n'))
'''