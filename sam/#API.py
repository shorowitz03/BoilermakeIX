
# Raw Package
import numpy as np
import pandas as pd

#Data Source
import yfinance as yf


apple= yf.Ticker("aapl")

# show actions (dividends, splits)
apple.actions

# show dividends
apple.dividends

# show splits
apple.splits

# + other methods etc.