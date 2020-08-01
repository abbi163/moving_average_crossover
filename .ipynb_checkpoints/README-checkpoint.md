Trading Strategy, Algorithmic Trading, S&P500, Python


### Moving Average Crossover
-------------------------------------------------


The moving average (MA) is a simple technical analysis tool that smooths out price data by creating a constantly updated average price. The average is taken over a specific period of time, like 10 days, 50 days, 200 days or any time period the trader chooses.

Moving average crossover is a strategy to apply when two moving averages on a chart: one longer and one shorter cross over each other. When the shorter-term MA crosses above the longer-term MA, it's a buy signal, as it indicates that the trend is shifting up. This is known as a "golden cross."

We will be using 10 day moving average as shorter-term MA and 50 day moving averages as longer-term MA. 

```python
aapl['MA10'] = aapl['Close'].rolling(10).mean()
aapl['MA50'] = aapl['Close'].rolling(50).mean()
aapl.head(2)
```

Here "aapl" is daily OHLC data of Apple stock.  

The tutorial of how to use moving average is explained in the file **'notebook/Moving_average_crossover.ipynb'**. 

Python script where moving average crossover strategy is applied to all the data is given in **Moving_average_crossover.py**

### Data Collection of S&P 500 stocks!





