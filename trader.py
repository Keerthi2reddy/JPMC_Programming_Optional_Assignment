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

class Trader:
    def __init__(self, name):
        self.name = name
