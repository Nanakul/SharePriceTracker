import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf
import time
from datetime import datetime

# Set Current date
today = datetime.now().date().strftime('%Y-%m-%d')

# Ask user to input the symbol of the company they want to track.
select_stock = (input('Please enter the symbol of the company you would like to track: '))
selected_stock = yf.Ticker(select_stock)


def print_info() -> None:
    """This function will print out the information of the company
    the user has input.
    """

    # Set variable for company to grab info
    stock_info = selected_stock.info

    # Display each value (line by line)
    for key, value in stock_info.items():
        print(key, ":", value)


def plot_dividends():
    """This function will grab dividend information about the company
    and plot the dividend history over user specified time frame.
    """
    # Create dividend dataframe variable of selected company    
    div_df = selected_stock.dividends

    # Resample data to retrieve sum of dividends by year 
    data_resample = div_df.resample('Y').sum()

    # Create new column in dataframe of extracted year
    data_resample = data_resample.reset_index()
    data_resample['Year'] = data_resample['Date'].dt.year

    min_year = (int(input('Enter the starting year of dividend history: ')))
    max_year = (int(input('Enter the ending year of dividend history: ')))

    # Plotting out a graph of Microsoft Dividend History
    plt.figure()
    plt.bar(data_resample['Year'], data_resample['Dividends'])
    plt.ylabel('Dividend Yield in $')
    plt.xlabel('Year')
    plt.title('Microsoft Dividend History')
    plt.xlim(min_year, max_year)
    plt.show()


def plot_history_close_price():
    """This function will plot the closing price history of the 
    given company from whenever the user specifies to the current date.
    """

    history_start = input('Starting date of history timeline? (year-month-day) Example: "2019-01-01": ')

    # See historical market data of given company
    stock_history = selected_stock.history(start=history_start, end=today)

    # Plotting out the Closing values from dates above.
    plt.figure()
    plt.plot(stock_history['Close'])
    plt.show()


if __name__ == '__main__':
    print_info()
    plot_dividends()
    plot_history_close_price()
