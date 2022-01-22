import sys 

stocks = [x.split(',')[0].strip(' ') for x in open('garrett\\nasdaq_screener_1642839777222.txt', 'r')]

sys.stdout = open('garrett/tickers.txt', 'w')

for x in stocks:
    print(x, end=',')