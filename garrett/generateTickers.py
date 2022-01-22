import sys 
import numpy as np
import pandas as pd
import yfinance as yf

stocks = [x.split(',')[0].strip(' ') for x in open('garrett\\nasdaq_screener_1642839777222.txt', 'r')]

file = open('garrett/tickers.txt', 'w')
    
for s in stocks:
    try:
        data = yf.download(tickers=s, period='2m', interval='1m', progress=False)
        file.write(s + ',')
        print(data)
        print(s + ' added')
    except:
        print(s + ' not found')