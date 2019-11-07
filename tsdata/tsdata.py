from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import pandas as pd

def produce_the_first(ticker, updateProgreeBar):
	weekly, weekly_meta_data = ts.get_weekly_adjusted(symbol=ticker)
	weekly.index = weekly.index.strftime('%Y-%m-%d')
	updateProgreeBar()

	ema, ema_metadata  = ti.get_ema(symbol=ticker, interval='weekly', time_period=26, series_type='close')
	ema.index = ema.index.strftime('%Y-%m-%d')
	updateProgreeBar()

	macd, macd_metadata = ti.get_macd(symbol=ticker, interval='weekly', series_type='close')
	macd.index = macd.index.strftime('%Y-%m-%d')
	updateProgreeBar()

	price = weekly.loc[:, "1. open": "4. close"]
	df = pd.concat([price, ema, macd], axis=1, join='inner')
	df = df.dropna(how='any')

	df.to_json(r'{}_first_screen.json'.format(ticker), orient='index')
	updateProgreeBar()

def produce_the_second(ticker, updateProgreeBar):
	daily, daily_meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
	daily.index = daily.index.strftime('%Y-%m-%d')
	updateProgreeBar()

	ema, ema_metadata  = ti.get_ema(symbol=ticker, interval='daily', time_period=22, series_type='close')
	ema.index = ema.index.strftime('%Y-%m-%d')
	updateProgreeBar()

	macd, macd_metadata = ti.get_macd(symbol=ticker, interval='daily', series_type='close')
	macd.index = macd.index.strftime('%Y-%m-%d')
	updateProgreeBar()

  # Calculate Force Index
	volume = daily.loc[:, "6. volume"]
	close = daily.loc[:, "4. close"]
	FI = close.diff().multiply(volume)

  # Calculate 2-day EMA of Force Index
	FI_2EMA = pd.Series.ewm(FI, span=2).mean()

	price = daily.loc[:, "1. open": "4. close"]
	df = pd.concat([price, ema, macd, FI.rename("FI"), FI_2EMA.rename("FI_2EMA")], axis=1, join='inner')
	df = df.dropna(how='any')

	df.to_json(r'{}_second_screen.json'.format(ticker), orient='index')
	updateProgreeBar()

def init(key):
	global ti
	ti = TechIndicators(key, output_format='pandas')
	global ts
	ts = TimeSeries(key, output_format='pandas')

