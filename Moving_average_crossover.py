# Moving Average Crossover Trading strategy!

import os
import numpy as np
import pandas as pd

# wealth_return function takes stock data as input and return buy price and net profit as output
def wealth_return(stock):
    stock['MA10'] = stock['Close'].rolling(10).mean()
    stock['MA50'] = stock['Close'].rolling(50).mean()
    stock = stock.dropna()
    #Add a new column "Shares", if MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)
    stock['Shares'] = [1 if stock.loc[ei, 'MA10']>stock.loc[ei, 'MA50'] else 0 for ei in stock.index]
    # restrucuring such that if share == 0 then only proceed !!
    if stock.iloc[0,-1] == 1:
        for i in range(len(stock)):
            if stock.iloc[i, -1] == 0:
                stock = stock.iloc[i:, :]
                break
                
    stock['Close1'] = stock['Close'].shift(-1)
    stock['Profit'] = [stock.loc[ei, 'Close1'] - stock.loc[ei, 'Close'] 
                       if stock.loc[ei, 'Shares']==1 else 0 for ei in stock.index]
    stock['wealth'] = stock['Profit'].cumsum()
    buy_price = list(stock[stock['Shares'] == 1]['High'])[0]
    net_profit = stock.loc[stock.index[-2], 'wealth']
    return buy_price, net_profit


# Folder where data is saved!
year = '2019_2020'
folder = 'S&P500/' + year
files = os.listdir(folder)

# saving the result into result array!!
result = []
for file in files:
    if file.endswith('.csv'):
        dataframe = pd.read_csv(folder + '/' +file)
        try:
            buy_price, net_profit = wealth_return(dataframe)
            ratio_profit = (net_profit/buy_price) * 100
            result.append((file.split('_')[0], buy_price, net_profit, ratio_profit))
        except (KeyError, IndexError):
            print(file)
stock_result = pd.DataFrame(data = result, columns = ['Symbol', 'Buy_price', 'Net_wealth', 'Profit_ratio'])   

# merging the files to show sector wise result
data = pd.read_csv('S&P500_ticker.csv')
final_result = stock_result.merge(data, left_on='Symbol', right_on='Symbol')
final_result.to_csv('Stock_gain_loss/' + year + '.csv', index = None)


