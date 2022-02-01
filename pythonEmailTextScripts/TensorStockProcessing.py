import yfinance as yf
import matplotlib

df = yf.download("TSLA", start="2018-11-01", end="2020-10-18", interval="1d")
df.head()
t = yf.Ticker("T")
t.dividends

t.dividends.plot(figsize=(14, 7))

