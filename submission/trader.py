# Trader
# a. Has access to an Order management system
# b. Has a bank account with a fixed amount of money in it.
# c. An action
# i. An action is defined as either a buy or a sell decision on a stock
# ii. The price at which the buy or sell order is placed should be randomized between
# the below three options
# 1. Place order at best bid
# 2. Place order at best ask
# 3. Place order at mid price ( mid price = (best bid + best ask) /2 )
# 4. Assume the size of the order placed (quantity) is always 1000.5. If there are no bids or offers present in the market, the trader places a
# buy or sell order arbitrarily 5% above or below the previous closing price.

from order_management_system import OrderManagementSystem
import random


class Trader:
    def __init__(self, name, portfolio, balance=100000):
        self.name = name
        self.balance = balance
        self.portfolio = portfolio
        self.oms = OrderManagementSystem(name, self.portfolio, balance, 0)

    def add_money(self, amount):
        self.oms.account_balance += amount

    def action(self, stock_exchange, share, order_type):
        if order_type == 'buy':
            self.buy_stock(stock_exchange, share)
        else:
            self.sell_stock(stock_exchange, share)

    def buy_stock(self,stock_exchange, share):
        best_bid, best_offer = stock_exchange.best_bid_and_offer(share.name)

        random_option = random.randint(1, 4)

        if random_option == 1 and best_bid:
            price = best_bid * 0.95
        elif random_option == 2 and best_offer:
            price = best_offer * 1.05
        elif random_option == 3 and best_bid and best_offer:
            price = (best_bid + best_offer) / 2
        else:
            price = share.price * random.uniform(0.95, 1.05)

        self.oms.buy_stock(self,stock_exchange,share.name, 1000, price)

    def sell_stock(self, stock_exchange, share):
        best_bid, best_offer = stock_exchange.best_bid_and_offer(share.name)

        random_option = random.randint(1, 4)

        if random_option == 1 and best_bid:
            price = best_bid * 0.95
        elif random_option == 2 and best_offer:
            price = best_offer * 1.05
        elif random_option == 3 and best_bid and best_offer:
            price = (best_bid + best_offer) / 2
        else:
            price = share.price * random.uniform(0.95, 1.05)
        self.oms.sell_stock(self,stock_exchange,share.name, 1000, price)
