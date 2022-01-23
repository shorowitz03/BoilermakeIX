import yfinance as yf
import pandas as pd
import pandas as pd
import numpy as np
import mplcyberpunk
from matplotlib import style
style.use('dark_background')
import matplotlib.pyplot as plt
from makeGraphs import * 

fileLines = open('garrett\\template.html', 'r').readlines()

span = '3mo'
top, bottom, sp_500_yf_df = getEnds(span)

for i, ticker in enumerate(bottom):
    stock = yf.Ticker(ticker).info
    path = 'mysite\static\image\\bottomStock{i}.jpg'.format(i=i+1)
    with open('mysite\\templates\\bottomStock{i}.html'.format(i=i+1), 'w') as f:
        for line in fileLines:
            message = line.format(  IMG_PATH    = path,
                                    LONG_BIO    = stock['longBusinessSummary'],
                                    OPEN_VAL    = stock['open'],
                                    PRICE       = stock['currentPrice'],
                                    TICKER      = ticker,
                                    NAME        = stock['longName'])
            f.write(message)
    with open('mysite\\templates\\bottomStock{i}.html'.format(i=i+1), 'r') as f: data = f.read().replace('~', '{').replace('*', '}')
    with open('mysite\\templates\\bottomStock{i}.html'.format(i=i+1), 'w') as f: f.write(data)
    
    
for i, ticker in enumerate(top):
    stock = yf.Ticker(ticker).info
    path = 'mysite\static\image\\topStock{i}.jpg'.format(i=i+1)
    with open('mysite\\templates\\topStock{i}.html'.format(i=i+1), 'w') as f:
        for line in fileLines:
            message = line.format(  IMG_PATH    = path,
                                    LONG_BIO    = stock['longBusinessSummary'],
                                    OPEN_VAL    = stock['open'],
                                    PRICE       = stock['currentPrice'],
                                    TICKER      = ticker,
                                    NAME        = stock['longName'])
            f.write(message)
    with open('mysite\\templates\\topStock{i}.html'.format(i=i+1), 'r') as f: data = f.read().replace('~', '{').replace('*', '}')
    with open('mysite\\templates\\topStock{i}.html'.format(i=i+1), 'w') as f: f.write(data)
