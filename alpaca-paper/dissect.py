"""
File: disset.py 
-------------------
This file is for disseting the Alpaca API to gain
more information about the objects.
"""

from config import * # imports everything from config.py 
import alpaca_trade_api as tradeapi # for working with the Alpaca SDK 

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL)


"""
When defining object classes, you can declare a 
__repr__ function which holds all of the class 
attributes. In this file, we will make us of it
for dissecting Alpaca object classes. 
"""

account = api.get_account() # connect the account to the API 

# dissect the account object that was instantiated
print("Account information: \n", repr(account))
""" 
>>> prints something like this: 
Account information: 
 Account({   'account_blocked': False,
    'account_number': 'API_KEY',
    'buying_power': '399874.09',
    'cash': '99874.09',
    'created_at': '2021-03-16T13:56:51.19951Z',
    'currency': 'USD',
    'daytrade_count': 0,
    'daytrading_buying_power': '399874.09',
    'equity': '99999.87',
    'id': 'YOUR_ID',
    'initial_margin': '62.89',
    'last_equity': '100000',
    'last_maintenance_margin': '0',
    'long_market_value': '125.78',
    'maintenance_margin': '37.734',
    'multiplier': '4',
    'pattern_day_trader': False,
    'portfolio_value': '99999.87',
    'regt_buying_power': '199873.96',
    'short_market_value': '0',
    'shorting_enabled': True,
    'sma': '0',
    'status': 'ACTIVE',
    'trade_suspended_by_user': False,
    'trading_blocked': False,
    'transfers_blocked': False})
"""
# we can now use the dot operator to get any of this information





