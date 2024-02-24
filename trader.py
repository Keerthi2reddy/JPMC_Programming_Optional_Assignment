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
from stock_exchange import StockExchange

class Trader:
    def __init__(self, name, balance=1000000):
        self.name = name
        self.balance = balance
        self.portfolio = []
        self.initialize_portfolio()
        self.oms = OrderManagementSystem(name, self.portfolio, balance, )

    def initialize_portfolio(self):
        self.portfolio = [{'stock_name': 'Google', 'quantity': 100, 'buy_price': 1000},
                          {'stock_name': 'Apple', 'quantity': 100, 'buy_price': 200},
                          {'stock_name': 'Microsoft', 'quantity': 100, 'buy_price': 300}]

    def add_money(self, amount):
        self.balance += amount

    def action(self, stock_exchange, share, order_type):
        if order_type == 'buy':
            self.buy_stock(stock_exchange, share)
        else:
            self.sell_stock(stock_exchange, share)

    def buy_stock(self, stock_exchange, share):
        stock = stock_exchange.get_stock(share)
        # randomize the price
        if stock['best_bid'] and stock['best_ask']:
            price = (stock['best_bid'] + stock['best_ask']) / 2
        elif stock['best_bid']:
            price = stock['best_bid'] * 0.95
        elif stock['best_ask']:
            price = stock['best_ask'] * 1.05
        else:
            price = stock['previous_close'] * 0.95 if stock['previous_close'] else 100
        self.oms.buy_stock(stock['name'], 1000, price)

    def sell_stock(self, stock_exchange, share):
        stock = stock_exchange.get_stock(share)
        # randomize the price
        if stock['best_bid'] and stock['best_ask']:
            price = (stock['best_bid'] + stock['best_ask']) / 2
        elif stock['best_bid']:
            price = stock['best_bid'] * 0.95
        elif stock['best_ask']:
            price = stock['best_ask'] * 1.05
        else:
            price = stock['previous_close'] * 1.05 if stock['previous_close'] else 100
        self.oms.sell_stock(stock['name'], 1000, price)

    

