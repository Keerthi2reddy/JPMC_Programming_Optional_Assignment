# An Order management system for a trader
# a. A method to track the trader’s cash in the trading account
# b. A method to add and withdraw cash from the trading account.
# c. A method that indicates the current value of the trader’s portfolio
# d. A method to place buy orders.
# e. A method to place sell orders.

class OrderManagementSystem:
    def __init__(self, trader_name, portfolio, account_balance = 0, portfolio_value = 0):
        self.trader_name = trader_name
        self.account_balance = account_balance
        self.portfolio = portfolio # list of dictionaries, where each dictionary is stock_name, quantity, buy_price
        self.portfolio_value = portfolio_value

    def get_balance(self):
        return self.account_balance
    
    def get_portfolio_value(self):
        return self.portfolio_value
    
    def show_portfolio(self):
        for stock in self.portfolio:
            print(stock)
        return self.portfolio
    
    def buy_stock(self, stock_name, quantity, buy_price):
        self.account_balance -= (quantity * buy_price)
        self.portfolio.append({'stock_name': stock_name, 'quantity': quantity, 'buy_price': buy_price})

    def sell_stock(self, stock_name, quantity, sell_price):
        found = 0
        for stock_dict in self.portfolio:
            if stock_dict['stock_name'] == stock_name:
                found = 1
                if stock_dict['quantity'] >= quantity:
                    stock_dict['quantity'] -= quantity
                    self.account_balance += (quantity * sell_price)
                    if stock_dict['quantity'] == 0:
                        sold_stock = stock_dict
                        self.portfolio.remove(stock_dict)

        if found == 0:
            print('Stock not found in portfolio')
            sold_stock = None

        return sold_stock