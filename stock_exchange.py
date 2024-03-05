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
from trader import Trader

class StockExchange:
    def __init__(self):
        self.last_traded_price = {}
        self.best_bid = {}
        self.best_offer = {}
        self.top_5_bids = {}
        self.top_5_offers = {}
        self.trading_hours = (0, 23400)  # Trading hours from 9 AM to 4 PM
        self.order_queue = {}
        self.order_id = 0
        self.securities = ['Google', 'AAPL', 'MSFT', 'AMZN', 'FB']
        self.initiate_securities()

    def initiate_securities(self):
        # Initialize securities with empty bid and offer dictionaries
        for security in self.securities:
            self.top_5_bids[security] = []
            self.top_5_offers[security] = []

    def last_traded_price(self, security):
        return self.last_traded_price.get(security, None)

    def best_bid_and_offer(self, security):
        return self.best_bid.get(security, None), self.best_offer.get(security, None)

    def top_5_bids_and_offers(self, security):
        return self.top_5_bids.get(security, None), self.top_5_offers.get(security, None)
    
    def accept_order(self, trader, security, order_type, price, quantity,current_time):
        if self._is_trading_hour(current_time):
            if order_type == "bid":
                order_list = self.top_5_bids
                best_price = lambda x: -x[1]  # Sort by price descending for bids
            elif order_type == "offer":
                order_list = self.top_5_offers
                best_price = lambda x: x[1]  # Sort by price ascending for offers
            else:
                self.notify(trader.name, "Invalid order type. Please specify 'bid' or 'offer'.")
                return False

            if security not in order_list:
                self.notify(trader.name, f"Your {order_type} is cancelled.")
                return False

            order_list[security].append((trader, price, quantity))
            order_list[security].sort(key=best_price)  # Sort based on the specified lambda function

            if len(order_list[security]) > 5:
                order_list[security] = order_list[security][:5]
                least_order = order_list[security][-1]  # Get the least order
                self.notify(least_order[0], f"Your {order_type} at price {least_order[1]} has been cancelled as it is not among the top 5.")

            if order_type == "bid":
                self.best_bid[security] = order_list[security][0][1] if order_list[security] else None
            else:
                self.best_offer[security] = order_list[security][0][1] if order_list[security] else None

            return True
        else:
            self.notify(trader.name, "Your order is cancelled as trading hours are done.")
            return False

        
    def match_orders(self,current_time):
        if not self._is_trading_hour(current_time):
            return False

        # Implement order matching algorithm following price-time priority
        # This is a simplified version assuming continuous trading
        for security in self.top_5_bids:
            if security in self.top_5_offers:
                for bid in self.top_5_bids[security]:
                    for offer in self.top_5_offers[security]:
                        if bid[1] >= offer[1]:  # Check if bid price is greater than or equal to offer price
                            quantity = min(bid[2], offer[2])  # Match minimum of bid and offer quantity
                            # Execute trade
                            self._execute_trade(bid[0], offer[0], security, offer[1], quantity)
                            # Update bid and offer quantities
                            
                            bid = list(bid)
                            offer = list(offer)
                            
                            oindex = self.top_5_offers[security].index(tuple(offer))
                            bindex = self.top_5_bids[security].index(tuple(bid))

                            # Modify quantity in the bid and offer lists
                            bid[2] -= quantity
                            offer[2] -= quantity
                            self.top_5_offers[security][oindex] = tuple(offer)
                            self.top_5_bids[security][bindex] = tuple(bid)

                            if bid[2] == 0:
                                self.top_5_bids[security].remove(tuple(bid))
                            if offer[2] == 0:
                                self.top_5_offers[security].remove(tuple(offer))
                            if len(self.top_5_bids[security]) == 0 or len(self.top_5_offers[security]) == 0:
                                break

    def _execute_trade(self, buyer, seller, security, price, quantity):
        # Perform trade execution (update balances, transfer shares, etc.)
        
        # Calculate the total cost of the shares
        total_cost = price * quantity

        # Check if the buyer has enough funds
        if buyer.balance >= total_cost:
            # Transfer shares and funds
            buyer.balance -= total_cost
            seller.balance += total_cost
            # Update buyer's portfolio
            self.update_buyer_portfolio(buyer, security, price, quantity)

            # Update seller's portfolio with the trade
            self.update_seller_portfolio(seller, security, price, quantity)

            # Update last traded price
            self.last_traded_price[security] = price

            # Notify traders about the trade
            self.notify(buyer.name, f"You have bought {quantity} shares of {security} at price {price}.")
            self.notify(seller.name, f"You have sold {quantity} shares of {security} at price {price}.")
        else:
            # Notify buyer about insufficient funds
            self.notify(buyer.name, "Insufficient funds to complete the purchase.")
        
    def update_buyer_portfolio(self, trader, security, price, quantity):
        # Update the trader's portfolio with the bought quantity of the stock
        for holding in trader.portfolio:
            if holding['stock_name'] == security:
                holding['quantity'] += quantity
                return
            
    def update_seller_portfolio(self, trader, security, price, quantity):
        # Deduct the sold quantity of the stock from the trader's portfolio
        for holding in trader.portfolio:
            if holding['stock_name'] == security:
                holding['quantity'] -= quantity
                return

    def end_trading_day(self):
        # Cancel any pending orders and notify traders
        for security in self.top_5_bids:
            for bid in self.top_5_bids[security]:
                self.notify(bid[0], "Your bid is cancelled as the trading day has ended.")
            # Notify trader about cancelled bid
                pass
        for security in self.top_5_offers:
            for offer in self.top_5_offers[security]:
                self.notify(offer[0], "Your offer is cancelled as the trading day has ended.")
            # Notify trader about cancelled offer
                pass
        # Clear top bids and offers
        self.top_5_bids = {}
        self.top_5_offers = {}
    
    def notify(self, trader_id, message):
        # Send notification to the trader
        print(f"Trader {trader_id}: {message}")
    
    def _is_trading_hour(self, current_time):
      return self.trading_hours[0] <= current_time <= self.trading_hours[1]
