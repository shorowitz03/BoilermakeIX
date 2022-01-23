import yfinance as yf
import pandas as pd
import numpy as np
import mplcyberpunk
from matplotlib import style
style.use('cyberpunk')
import matplotlib.pyplot as plt
import seaborn as sns

ticker = 'AAPL'

prices = yf.download(ticker, period='3mo', auto_adjust=True)['Closed'] # downloads tesla stock data
date_time = prices.copy(deep=True).reset_index()['Date']               # gets only the dates

sns.lineplot(data=prices)
sns.set_theme()  # Default seaborn style
plt.xticks(rotation=30)
plt.title(f"Closing Stock Prices for {ticker}")
plt.show()