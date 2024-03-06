# import classes from the directory entities

from share import Share
from stock_exchange import StockExchange
from trader import Trader
from order_management_system import OrderManagementSystem
# import time
import time
import random
import logging

random.seed(7)

# initialise the stock exchange
stock_exchange = StockExchange()

# initialized the shares
shareA = Share("Google", 50)
shareB = Share("Apple", 20)
shareC = Share("Microsoft", 30)

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


logging.basicConfig(filename='trader_balances.log',level=logging.INFO)  # Set the logging level to INFO

# for each second
for i in range(23400):
    logging.info(f"\n\n\nTime: {i + 1}")
    for trader in [traderA, traderB, traderC, traderD, traderE]:
        action(trader, random.choice(["buy", "sell"]), random.choice([shareA, shareB, shareC]))
        # if trader has run out of money, deposit random amount
        if trader.oms.account_balance <= 1000:
            trader.add_money(random.randint(1, 1000)*1000)   
    stock_exchange.match_orders()

# print the pending orders
logging.warning("\n\nPending orders")
stock_exchange.end_trading_day()

logging.info("\n\nFinal balances")
for trader in [traderA, traderB, traderC, traderD, traderE]:
    logging.info(f'{trader.name}\'s balance: {trader.balance}')
