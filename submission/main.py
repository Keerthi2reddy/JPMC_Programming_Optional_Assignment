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

print()
print("Welcome to the stock exchange!")
print("The shares available for trading are Google, Apple, Microsoft, Amazon and Facebook.")
print("The length of the trading day is 6.5 hours, or 23400 seconds.")
print()

# initialized 5 traders
traderA = Trader("John", [(shareA, 10000), (shareB, 20000), (shareC, 30000)], 1000000)
traderB = Trader("Jane", [(shareA, 150000), (shareB, 50000), (shareC, 20000)], 500000)
traderC = Trader("Jack", [(shareA, 50000), (shareB, 10000), (shareC, 15000)], 2000000)
traderD = Trader("Jill", [(shareA, 250000), (shareB, 30000), (shareC, 40000)], 3000000)
traderE = Trader("James", [(shareA, 350000), (shareB, 40000), (shareC, 50000)], 4000000)

trader_colors = {
    "John": "\033[31m",
    "Jane": "\033[32m",
    "Jack": "\033[33m",
    "Jill": "\033[34m",
    "James": "\033[35m"
}

print(f"The traders are {trader_colors['John']}John\033[0m, {trader_colors['Jane']}Jane\033[0m, {trader_colors['Jack']}Jack\033[0m, {trader_colors['Jill']}Jill\033[0m and {trader_colors['James']}James.\033[0m")
print(f"{trader_colors['John']}John\033[0m has a balance of 1000000 and 10000 shares of Google, 20000 shares of Apple and 30000 shares of Microsoft.")
print(f"{trader_colors['Jane']}Jane \033[0mhas a balance of 500000 and 150000 shares of Google, 50000 shares of Apple and 20000 shares of Microsoft.")
print(f"{trader_colors['Jack']}Jack\033[0m has a balance of 2000000 and 50000 shares of Google, 10000 shares of Apple and 15000 shares of Microsoft.")
print(f"{trader_colors['Jill']}Jill\033[0m has a balance of 3000000 and 250000 shares of Google, 30000 shares of Apple and 40000 shares of Microsoft.")
print(f"{trader_colors['James']}James\033[0m has a balance of 4000000 and 350000 shares of Google, 40000 shares of Apple and 50000 shares of Microsoft.")
print()

def action(trader, type, share):
    if type == "buy":
        trader.buy_stock(stock_exchange, share)
    else:
        trader.sell_stock(stock_exchange, share)


logging.basicConfig(filename='trader_balances.log',level=logging.INFO)  # Set the logging level to INFO

print("Running simulation now...")

# for each second
for i in range(23400):
    logging.info(f"\n\n\nTime: {i + 1}")
    if (i + 1) % 1000 == 0: # print the time every 1000 seconds on the terminal
        print(f"We are at time: {i + 1}. Time remaining: {23400 - (i + 1)}.")
    for trader in [traderA, traderB, traderC, traderD, traderE]:
        action(trader, random.choice(["buy", "sell"]), random.choice([shareA, shareB, shareC]))
        # if trader has run out of money, deposit random amount
        if trader.oms.account_balance <= 1000:
            trader.add_money(random.randint(1, 1000)*1000)   
    stock_exchange.match_orders()


print()
print()
print("Trading day has ended. Check the trader_balances.log file for the every step of the simulation.")

# print the pending orders
logging.warning("\n\nPending orders")
stock_exchange.end_trading_day()

logging.info("\n\nFinal balances")
for trader in [traderA, traderB, traderC, traderD, traderE]:
    print(f'{trader_colors[trader.name]}{trader.name}\'s\033[0m balance: {trader.balance}')
    logging.info(f'{trader.name}\'s balance: {trader.balance}')

print()
print("Thanks for trading :)")
print()