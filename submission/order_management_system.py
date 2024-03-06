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
        self.portfolio = []
        # make the portfolio a list of dictionaries
        for stock in portfolio:
            self.portfolio.append({'stock_name': stock[0].name, 'quantity': stock[1]})
        self.portfolio_value = portfolio_value

    def get_balance(self):
        return self.account_balance
    
    def get_portfolio_value(self):
        return self.portfolio_value
    
    def show_portfolio(self):
        for stock in self.portfolio:
            print(stock)
        return self.portfolio
    
    def buy_stock(self,trader,stock_exchange, stock_name, quantity, buy_price):
        stock_exchange.accept_order(trader, stock_name, 'bid', buy_price, quantity)


    def sell_stock(self,trader,stock_exchange, stock_name, quantity, sell_price):
        stock_exchange.accept_order(trader, stock_name, 'offer', sell_price, quantity)