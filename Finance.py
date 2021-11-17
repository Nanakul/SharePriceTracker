import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
from datetime import datetime

# Set Current date
today = datetime.now().date().strftime('%Y-%m-%d')

# Ask user to select company to track 
# And save ticker as a variable
select_stock = (input('Please enter the symbol of the company you would like to track: '))
selected_stock = yf.Ticker(select_stock)

# Set variable for company to grab info
stock_info = selected_stock.info

# Display each value (line by line)
for key,value in stock_info.items():
    print(key, ":", value)

# Create dividend dataframe variable of selected company    
div_df = selected_stock.dividends

# Resample data to retrieve sum of dividends by year 
data_resample = div_df.resample('Y').sum()

# Create new column in dataframe of extracted year
data_resample = data_resample.reset_index()
data_resample['Year'] = data_resample['Date'].dt.year

# Plotting out a graph of Microsoft Dividend History
plt.figure()
plt.bar(data_resample['Year'], data_resample['Dividends'])
plt.ylabel('Dividend Yield in $')
plt.xlabel('Year')
plt.title('Microsoft Dividend History')
plt.xlim(2002,2020)
plt.show()

# See historical market data of given company
stock_history = selected_stock.history(start='2019-01-01', end=today)

# Plotting out the Closing values from dates above.
plt.figure()
plt.plot(stock_history['Close'])
plt.show()