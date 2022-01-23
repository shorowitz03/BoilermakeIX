import yfinance as yf
import pandas as pd
import pandas as pd
import numpy as np
import mplcyberpunk
from matplotlib import style
style.use('cyberpunk')
import matplotlib.pyplot as plt


''' gets data from a few stocks and plots it
startDate = '2020-01-01'

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

span = '3mo'

#pulls the s&p 500 stocks
sp_500_tickers = pd.read_html('https://en.wikipedia.org/wiki/List_of_S%26P_500_companies')[0]
sp_500_yf_df = yf.download(sp_500_tickers.Symbol.to_list(), period=span, auto_adjust=True)['Close']
lastDate = sp_500_yf_df.copy(deep=True).reset_index()['Date'].iloc[-1]
cum_return = (sp_500_yf_df.copy(deep=True).pct_change() + 1).cumprod()
sorted_df  = cum_return.sort_values(by=lastDate ,axis=1, na_position='last')

#removes colums that yf can not pull
while(np.isnan(sorted_df.iloc[-1, -1])):
    print('loop activated')
    sorted_df = sorted_df.iloc[:, :-1]
    
# gets the bottom and top five stocks
bottom = sorted_df.columns.values.tolist()[0:5]
top    = sorted_df.columns.values.tolist()[-5:]

for i, ticker in enumerate(top):
    plt.clf()
    sp_500_yf_df[ticker].plot()
    plt.legend()
    plt.title("Top #{i} Daily {span} Returns ({ticker})".format(i=i+1, span=span, ticker=ticker), fontsize=16)
    plt.ylabel('Cumulative Stock Returns', fontsize=14)
    plt.xlabel('Date', fontsize=14)

    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.savefig('mysite\static\image\\topStock{i}.jpg'.format(i=i+1))
for i, ticker in enumerate(bottom):
    plt.clf()
    sp_500_yf_df[ticker].plot()
    plt.legend()
    plt.title("Bottom #{i} Daily {span} Returns ({ticker})".format(i=i+1, span=span, ticker=ticker), fontsize=16)
    plt.ylabel('Day Closing Value', fontsize=14)
    plt.xlabel('Date', fontsize=14)

    plt.grid(which="major", color='k', linestyle='-.', linewidth=0.5)
    plt.savefig('mysite\static\image\\bottomStock{i}.jpg'.format(i=i+1))