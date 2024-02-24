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
    def __init__(self):
        self.last_traded_price = None
        self.best_bid = None
        self.best_offer = None
        self.top_5_bids = []
        self.top_5_offers = []
        self.trading_hours = set(range(9, 17))  # Trading hours from 9 AM to 4 PM
        self.orders = []

    def indicate_last_traded_price(self):
        return self.last_traded_price

    def indicate_best_bid_and_offer(self):
        return self.best_bid, self.best_offer

    def indicate_top_5_bids_and_offers(self):
        return self.top_5_bids, self.top_5_offers

    def accept_order(self, order):
        if order['price'] >= self.best_bid:
            self.best_bid = order['price']
        if order['price'] <= self.best_offer:
            self.best_offer = order['price']

        if order['type'] == 'buy':
            self.top_5_bids.append(order)
            self.top_5_bids.sort(key=lambda x: (-x['price'], x['timestamp']))
        else:
            self.top_5_offers.append(order)
            self.top_5_offers.sort(key=lambda x: (x['price'], x['timestamp']))

        self.orders.append(order)

    def order_matching_engine(self, order):
        if order['type'] == 'buy':
            matching_orders = [o for o in self.top_5_offers if o['price'] <= order['price']]
            if matching_orders:
                matched_order = matching_orders[0]
                self.last_traded_price = matched_order['price']
                self.exchange_money_and_shares(order, matched_order)
        else:
            matching_orders = [o for o in self.top_5_bids if o['price'] >= order['price']]
            if matching_orders:
                matched_order = matching_orders[0]
                self.last_traded_price = matched_order['price']
                self.exchange_money_and_shares(order, matched_order)

    def exchange_money_and_shares(self, buyer_order, seller_order):
        buyer_money = buyer_order['quantity'] * seller_order['price']
        seller_money = seller_order['quantity'] * seller_order['price']

        print(f"Money transferred: Buyer pays {seller_money}, Seller receives {seller_money}")
        print("Shares transferred.")

        self.top_5_bids.remove(seller_order)
        self.top_5_offers.remove(buyer_order)

    def cancel_orders_outside_top_5(self):
        if len(self.top_5_bids) > 5:
            for order in self.top_5_bids[5:]:
                print(f"Order {order} cancelled, not in top 5 bids.")
            self.top_5_bids = self.top_5_bids[:5]

        if len(self.top_5_offers) > 5:
            for order in self.top_5_offers[5:]:
                print(f"Order {order} cancelled, not in top 5 offers.")
            self.top_5_offers = self.top_5_offers[:5]

    def cancel_pending_orders_at_end_of_day(self):
        if not self.trading_hours:
            for order in self.orders:
                print(f"Order {order} cancelled, end of trading day.")
            self.orders = []
