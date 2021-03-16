"""
File: functions.py 
-------------------
This file contains several functions
which allow a user to do common things 
in a simple way. 
"""

# takes in an account and returns buying power 
def get_buying_power(account):
	return account.buying_power


# gain/loss of portfolio on the day: 
def get_gain_loss(account): 
	difference = float(account.equity) - float(account.last_equity)
	return difference


# get historical data of an asset over the inputted amount of days
def get_historical_data(api, symbol, days):
	barset = api.get_barset(symbol, 'day', limit=days)
	bars = barset[symbol]
	return bars


# get the percent change over the inputted amount of days for an asset 
def get_percent_change(api, symbol, days):
	# first get the historical data bars
	bars = get_historical_data(api, symbol, days)
	w_open = bars[0].o
	w_close = bars[-1].c
	change = round(((w_close - w_open) / week_open * 100), 2)
	return change


# place an a regular market order 
def place_market_order(api, symbol, quantity):
	api.submit_order(
	    symbol=symbol,
	    qty=quantity,
	    side='buy',
	    type='market',
	    time_in_force='gtc'
	)	
