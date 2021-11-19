import yfinance as yf
import time
from datetime import datetime

# Ask user for company they'd like to track
select_stock = input('Please enter the symbol of the company you would like to track the share price of: ')
selected_stock = yf.Ticker(select_stock)


def track_current_price() -> list:
    """
    This function will track the current price of the given company
    and will print the current price every minute for one hour. It will
    store all the current prices into a text file.
    """

    # Minute Counter
    minutes_passed = 0

    # List of current prices
    price_list = []

    while minutes_passed != 60:
        # Update Time
        today = datetime.now()
        current_time = today.strftime('%I:%M:%S %p')
        # Selected company info == currentPrice
        current_price = selected_stock.info['currentPrice']

        # Create/Write to file the Company, Price, and Time
        with open('current_price.txt', 'a') as f:
            f.write('Company: ' + str(selected_stock)[23:].upper() + ' | ' +
                    'Price: ' + str(current_price) + ' | ' +
                    'Time: ' + current_time + '\n')
        time.sleep(60)
        minutes_passed += 1
        # List to store all prices in
        price_list.append(current_price)
        return price_list


def hour_max_price() -> float:
    max_price = track_current_price()
    float_max_price = float(max(max_price))
    return float_max_price


def get_max_price() -> None:
    max_price = hour_max_price()
    print(max_price)


if __name__ == '__main__':
    track_current_price()
    hour_max_price()
    get_max_price()
