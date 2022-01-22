from turtle import st
import yfinance as yf
import pandas as pd
import pandas as pd
import numpy as np
import mplcyberpunk
from matplotlib import style
style.use('cyberpunk')
import matplotlib.pyplot as plt
import tensorflow as tf


stockData = yf.download('TSLA', period='10y', auto_adjust=True) # downloads tesla stock data
date_time = stockData.copy(deep=True).reset_index()['Date'] #gets only the dates

# plots the trends over time
plot_cols = ['Close', 'Volume']
plot_features = stockData[plot_cols]
plot_features.index = date_time
_ = plot_features.plot(subplots=True)

plot_features = stockData[plot_cols][:480]
plot_features.index = date_time[:480]
_ = plot_features.plot(subplots=True)
plt.show()

# graphically shows what frequencies are important
fft = tf.signal.rfft(stockData['Close'])
f_per_dataset = np.arange(0, len(fft))
n_samples_h = len(stockData['Close'])
hours_per_year = 24*365.2524
years_per_dataset = n_samples_h/(hours_per_year)
f_per_year = f_per_dataset/years_per_dataset
plt.step(f_per_year, np.abs(fft))
plt.xscale('log')
plt.ylim(0, 400000)
plt.xlim([0.1, max(plt.xlim())])
plt.xticks([1, 365.2524], labels=['1/Year', '1/day'])
_ = plt.xlabel('Frequency (log scale)')
plt.show()






