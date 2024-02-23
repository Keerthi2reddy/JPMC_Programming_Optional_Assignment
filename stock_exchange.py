# A Stock Exchange:
# Which constitutes
# a. A method that indicates the last traded price of any security
# b. A method that indicates the current best bid and best offer
# c. A method that indicates the top 5 bids and top 5 offers.
# d. A method to accept bids or offers
# e. Order Matching Engine (
# i. The Matching engine must always follow price-time priority for all orders
# Price time priority: https://www.marketswiki.com/wiki/Price-time_priority
# ii. When a trade is matched, the exchange should collect money from the person
# buying the share and send it to the person selling it. The share should also change
# hands immediately.
# iii. Assume the exchange does not charge any fees for facilitating trades.
# iv. The Engine should only accept orders sent during the trading hours.
# v. Any bid or offer outside of the top 5 bids or top 5 offers is cancelled and the trader
# is notified. Any pending orders at the end of the day are cancelled and the trader
# is notified.

class StockExchange:
    def __init__(self, name):
        self.name = name