# import classes from the directory entities

from share import Share
from stock_exchange import StockExchange
from trader import Trader
from order_management_system import OrderManagementSystem

share = Share("Google")
stock_exchange = StockExchange("NYSE")
trader = Trader("John")
oms = OrderManagementSystem("OMS")
