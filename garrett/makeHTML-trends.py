import yfinance as yf
import pandas as pd
import pandas as pd
import numpy as np
import mplcyberpunk
from matplotlib import style
style.use('dark_background')
import matplotlib.pyplot as plt
from makeGraphs import * 

fileLines = [x for x in open('garrett\\template-trends.html', 'r')]

span = '3mo'
top, bottom, sp_500_yf_df = getEnds(span)
stonks = bottom + top

with open('mysite\\templates\\trends.html', 'w') as f:
    for i, line in enumerate(fileLines):
        if '**REPLACE**' in line:
            fileLines[i].replace('**REPLACE**', '')
            for ticker in stonks:
                stock = yf.Ticker(ticker).info
                for j in range(i, i + 6):
                    message = fileLines[j].format(  DTE         = stock['debtToEquity'],
                                                    P_MARG      = stock['profitMargins'],
                                                    PEG_RATIO   = stock['pegRatio'],
                                                    PRICE       = stock['currentPrice'],
                                                    TICKER      = ticker,
                                                    NAME        = stock['longName'])
                    f.write(message)
        else:
            f.write(line)
        
with open('mysite\\templates\\trends.html', 'r') as f: data = f.read().replace('~', '{').replace('*', '}')
with open('mysite\\templates\\trends.html', 'w') as f: f.write(data)

