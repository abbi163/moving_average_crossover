# Moving_Average_crossover
Trading Strategy, Algorithmic Trading, S&amp;P500, Python



## Moving Average Crossover

    In this notebook we will create a simple trading strategy using moving average crossover strategy. There are two kinds of signal we will be looking into for crossover strategy!
    a. Slow Signal: Moving average of relatively longer time period
    b. Fast Signal: Moving average of relatively shorter time period
    
**example:**

__1. M.A.(10 days) is fast signal when compared with M.A.(50 days)__

__2. M.A.(50 days) is fast signal when compared with M.A.(200 days)__   

        
    If fast signal cross over slow signal and is higher, we will buy the stock.
    If slow signal goes above fast signal we will sell the stock. 
    
    Note: If the fast signal is already above the slow signal, we won't enter the trade!


```python
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
%matplotlib inline
```

##### Checking Apple stock OHLC, Adj Close and volume 


```python
aapl = pd.read_csv('S&P500/2019_2020/AAPL_2019-01-01_2020-06-01.csv')
aapl.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-12-31</td>
      <td>158.529999</td>
      <td>159.360001</td>
      <td>156.479996</td>
      <td>157.740005</td>
      <td>154.618546</td>
      <td>35003500</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-01-02</td>
      <td>154.889999</td>
      <td>158.850006</td>
      <td>154.229996</td>
      <td>157.919998</td>
      <td>154.794983</td>
      <td>37039700</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 1: Adding fast and slow signal into the dataframe !


Note: We will be using 10 period and 50 period moving average as fast and slow signal


```python
aapl['MA10'] = aapl['Close'].rolling(10).mean()
aapl['MA50'] = aapl['Close'].rolling(50).mean()
aapl.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>0</th>
      <td>2018-12-31</td>
      <td>158.529999</td>
      <td>159.360001</td>
      <td>156.479996</td>
      <td>157.740005</td>
      <td>154.618546</td>
      <td>35003500</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
    <tr>
      <th>1</th>
      <td>2019-01-02</td>
      <td>154.889999</td>
      <td>158.850006</td>
      <td>154.229996</td>
      <td>157.919998</td>
      <td>154.794983</td>
      <td>37039700</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 2: Dropping all NaN values rows from MA10 and MA50


```python
aapl = aapl.dropna()
aapl.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>49</th>
      <td>2019-03-13</td>
      <td>182.250000</td>
      <td>183.300003</td>
      <td>180.919998</td>
      <td>181.710007</td>
      <td>178.878098</td>
      <td>31032500</td>
      <td>176.095001</td>
      <td>164.9172</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2019-03-14</td>
      <td>183.899994</td>
      <td>184.100006</td>
      <td>182.559998</td>
      <td>183.729996</td>
      <td>180.866608</td>
      <td>23579500</td>
      <td>177.153001</td>
      <td>165.4370</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 3 : Add a new column "Shares".

    If MA10>MA50, denote as 1 (long one share of stock), otherwise, denote as 0 (do nothing)


```python
aapl['Shares'] = [1 if aapl.loc[ei, 'MA10']>aapl.loc[ei, 'MA50'] else 0 for ei in aapl.index]
aapl.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
      <th>Shares</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>49</th>
      <td>2019-03-13</td>
      <td>182.250000</td>
      <td>183.300003</td>
      <td>180.919998</td>
      <td>181.710007</td>
      <td>178.878098</td>
      <td>31032500</td>
      <td>176.095001</td>
      <td>164.9172</td>
      <td>1</td>
    </tr>
    <tr>
      <th>50</th>
      <td>2019-03-14</td>
      <td>183.899994</td>
      <td>184.100006</td>
      <td>182.559998</td>
      <td>183.729996</td>
      <td>180.866608</td>
      <td>23579500</td>
      <td>177.153001</td>
      <td>165.4370</td>
      <td>1</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 4 : Restrucuring such that if shares == 1 then edit dataframe !!
    
    Note: If the fast signal is already above the slow signal, we will cut the dataframe such that the starting point is when Shares == 0


```python
if aapl.iloc[0,-1] == 1:
    for i in range(len(aapl)):
        if aapl.iloc[i, -1] == 0:
            aapl = aapl.iloc[i:, :]
            break
            
aapl.head(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
      <th>Shares</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>96</th>
      <td>2019-05-20</td>
      <td>183.520004</td>
      <td>184.350006</td>
      <td>180.279999</td>
      <td>183.089996</td>
      <td>180.930695</td>
      <td>38612300</td>
      <td>193.112999</td>
      <td>195.6952</td>
      <td>0</td>
    </tr>
    <tr>
      <th>97</th>
      <td>2019-05-21</td>
      <td>185.220001</td>
      <td>188.000000</td>
      <td>184.699997</td>
      <td>186.600006</td>
      <td>184.399307</td>
      <td>28364800</td>
      <td>191.487000</td>
      <td>195.8492</td>
      <td>0</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 5 : Calculating Profit !!
    Note: Profit is 0 if Shares = 0, i.e we aren't involved in any trading once Fast signal is below Slow signal!


```python
aapl['Close1'] = aapl['Close'].shift(-1)
aapl['Profit'] = [aapl.loc[ei, 'Close1'] - aapl.loc[ei, 'Close'] if aapl.loc[ei, 'Shares']==1 else 0 for ei in aapl.index]
aapl.tail(2)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
      <th>Shares</th>
      <th>Close1</th>
      <th>Profit</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>354</th>
      <td>2020-05-28</td>
      <td>316.769989</td>
      <td>323.440002</td>
      <td>315.630005</td>
      <td>318.250000</td>
      <td>318.250000</td>
      <td>33390200</td>
      <td>315.341003</td>
      <td>281.0924</td>
      <td>1</td>
      <td>317.940002</td>
      <td>-0.309998</td>
    </tr>
    <tr>
      <th>355</th>
      <td>2020-05-29</td>
      <td>319.250000</td>
      <td>321.149994</td>
      <td>316.470001</td>
      <td>317.940002</td>
      <td>317.940002</td>
      <td>38399500</td>
      <td>316.181003</td>
      <td>282.5178</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 6 : Calculating Wealth
    Wealth is cumsum of profit


```python
aapl['wealth'] = aapl['Profit'].cumsum()
aapl.tail(3)
```




<div>
<style scoped>
    .dataframe tbody tr th:only-of-type {
        vertical-align: middle;
    }

    .dataframe tbody tr th {
        vertical-align: top;
    }

    .dataframe thead th {
        text-align: right;
    }
</style>
<table border="1" class="dataframe">
  <thead>
    <tr style="text-align: right;">
      <th></th>
      <th>Date</th>
      <th>Open</th>
      <th>High</th>
      <th>Low</th>
      <th>Close</th>
      <th>Adj Close</th>
      <th>Volume</th>
      <th>MA10</th>
      <th>MA50</th>
      <th>Shares</th>
      <th>Close1</th>
      <th>Profit</th>
      <th>wealth</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <th>353</th>
      <td>2020-05-27</td>
      <td>316.140015</td>
      <td>318.709991</td>
      <td>313.089996</td>
      <td>318.109985</td>
      <td>318.109985</td>
      <td>28236300</td>
      <td>314.281003</td>
      <td>279.7846</td>
      <td>1</td>
      <td>318.250000</td>
      <td>0.140015</td>
      <td>107.439972</td>
    </tr>
    <tr>
      <th>354</th>
      <td>2020-05-28</td>
      <td>316.769989</td>
      <td>323.440002</td>
      <td>315.630005</td>
      <td>318.250000</td>
      <td>318.250000</td>
      <td>33390200</td>
      <td>315.341003</td>
      <td>281.0924</td>
      <td>1</td>
      <td>317.940002</td>
      <td>-0.309998</td>
      <td>107.129974</td>
    </tr>
    <tr>
      <th>355</th>
      <td>2020-05-29</td>
      <td>319.250000</td>
      <td>321.149994</td>
      <td>316.470001</td>
      <td>317.940002</td>
      <td>317.940002</td>
      <td>38399500</td>
      <td>316.181003</td>
      <td>282.5178</td>
      <td>1</td>
      <td>NaN</td>
      <td>NaN</td>
      <td>NaN</td>
    </tr>
  </tbody>
</table>
</div>



##### Step 7 : Calculating Buy price and net profit
    Note: Approximation: That we bought at the highest price on the day we purchased ! As it's daily price data and we don't know exactly at what price did we bought. So to be at safe side, we consider the highest price of purchase during that day. 


```python
buy_price = list(aapl[aapl['Shares'] == 1]['High'])[0]
net_profit = aapl.loc[aapl.index[-2], 'wealth']
profit_ratio = (net_profit/buy_price) * 100
print('Buy price: ${}, Net Profit: ${}, Profit Ratio: {}%'.format(buy_price, net_profit, round(profit_ratio, 3)))

```

    Buy price: $200.6100006103516, Net Profit: $107.12997436523449, Profit Ratio: 53.402%
    


