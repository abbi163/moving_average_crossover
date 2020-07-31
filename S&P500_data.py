# Download data for 1 year and 6 month from 2019-01-01 to 2020-06-01 for
# companies listed on S&P 500

import time
import pandas as pd
import yfinance as yf

# defining start date and end date
start_date = '2019-01-01'
end_date = '2020-06-01'

# variable where data will be saved
folder = 'S&P500/2019_2020/'

# extracting S&P500 companies stock ticker from CSV file
dataset = pd.read_csv('S&P500_ticker.csv')
symbols = list(dataset['Symbol'].values)

# downloading data and saving it into folder as csv files
for count, symbol in enumerate(symbols):
    if count%20==0:
        print(count//20)
        
    df = yf.download( symbol, 
                      start = start_date, 
                      end = end_date, 
                      progress=False)
    df.to_csv(folder +symbol+ '_' + start_date + '_' + end_date + '.csv',
              index = True)
    time.sleep(1)
print('data download finished')

