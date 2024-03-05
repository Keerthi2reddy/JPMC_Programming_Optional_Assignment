# import classes from the directory entities

from share import Share
from stock_exchange import StockExchange
from trader import Trader
from order_management_system import OrderManagementSystem
# import time
import time
import random
random.seed(7)

# share = Share("Google")
# stock_exchange = StockExchange()
# trader = Trader("John")
# oms = OrderManagementSystem("OMS")

#   [{'stock_name': 'Google', 'quantity': 100, 'buy_price': 1000},
#                           {'stock_name': 'Apple', 'quantity': 100, 'buy_price': 200},
#                           {'stock_name': 'Microsoft', 'quantity': 100, 'buy_price': 300}]

# initialise the stock exchange
stock_exchange = StockExchange()

# initialized the shares
shareA = Share("Google", 5000)
shareB = Share("Apple", 2000)
shareC = Share("Microsoft", 3000)

# initialized 5 traders
traderA = Trader("John", [(shareA, 10000), (shareB, 20000), (shareC, 30000)], 1000000)
traderB = Trader("Jane", [(shareA, 150000), (shareB, 50000), (shareC, 20000)], 500000)
traderC = Trader("Jack", [(shareA, 50000), (shareB, 10000), (shareC, 15000)], 2000000)
traderD = Trader("Jill", [(shareA, 250000), (shareB, 30000), (shareC, 40000)], 3000000)
traderE = Trader("James", [(shareA, 350000), (shareB, 40000), (shareC, 50000)], 4000000)

def action(trader, type, share):
    if type == "buy":
        trader.buy_stock(stock_exchange, share)
    else:
        trader.sell_stock(stock_exchange, share)


# Define color codes
colors = {
    'John': '\033[91m',  # Red
    'Jane': '\033[92m',  # Green
    'Jack': '\033[93m',  # Yellow
    'Jill': '\033[94m',  # Blue
    'James': '\033[95m'   # Purple
}

# Reset color
reset_color = '\033[0m'

# for each second
for i in range(23400):
    time.sleep(1)
    print(f"Time: {i + 1}")
    for trader in [traderA, traderB, traderC, traderD, traderE]:
        # Print trader's name in color
        print(f'{colors[trader.name]}{trader.name}{reset_color}', end = '')
        action(trader, random.choice(["buy", "sell"]), random.choice([shareA, shareB, shareC]))
        # if trader has run out of money, deposit random amount
        if trader.oms.account_balance <= 1000:
            trader.add_money(random.randint(1, 1000)*1000)
    print()

