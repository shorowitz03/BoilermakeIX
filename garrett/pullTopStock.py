import sys
import yfinance as yf
import pandas as pd
import pandas as pd
import numpy as np
import hvplot.pandas

import mplcyberpunk
from matplotlib import style
style.use('cyberpunk')

import matplotlib.pyplot as plt
import seaborn
# import tensorflow as tf

startDate = '2020-01-01'
''' gets data and plots it
tkrList = ['GOOG', 'AAPL', 'FB', 'TSLA']
data = yf.download(tkrList, startDate)['Adj Close']          #gets the data of the stock prices each day
dailyReturnData = round(data[tkrList].pct_change() * 100, 2)    #gets the percentage return values each day
print(dailyReturnData.tail(10))

((data.pct_change() + 1).cumprod()).plot()
plt.legend()
plt.title("Stock Daily Returns", fontsize=16)
plt.ylabel('Cumulative Stock Returns', fontsize=14)
plt.xlabel('Year', fontsize=14)

plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
plt.show()
'''

sp_500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
sp_500_yf_df = yf.download(sp_500_tickers.Symbol.to_list(), startDate, auto_adjust=True)['Close']


print(sp_500_yf_df.tail())

