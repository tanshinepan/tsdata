from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries
import pandas as pd
import os

os.environ['AV_KEY'] = 'abcde'
AV_KEY = os.getenv('AV_KEY')

ti = TechIndicators(AV_KEY, output_format='pandas')
ts = TimeSeries(AV_KEY, output_format='pandas')

def produce_weekly(ticker):
	weekly, weekly_meta_data = ts.get_weekly_adjusted(symbol=ticker)
	ema, ema_metadata  = ti.get_ema(symbol=ticker, interval='weekly', time_period=26, series_type='close')
	macd, macd_metadata = ti.get_macd(symbol=ticker, interval='weekly', series_type='close')
	price = weekly.loc[:, "1. open": "4. close"]
	df = pd.concat([price, ema, macd], axis=1, join='inner')
	df = df.dropna(how='any')
	return df

def calculate_fi(df):
  # Calculate Force Index
	volume = df.loc[:, "6. volume"]
	close = df.loc[:, "4. close"]
	FI = close.diff(-1).multiply(volume).iloc[::-1]

  # Calculate 2-day EMA of Force Index
	return FI, FI.ewm(span=2, adjust=False).mean().round()

def produce_daily(ticker):
	daily, daily_meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
	ema, ema_metadata  = ti.get_ema(symbol=ticker, interval='daily', time_period=22, series_type='close')
	macd, macd_metadata = ti.get_macd(symbol=ticker, interval='daily', series_type='close')
	fi, fi_ema = calculate_fi(df=daily)
	price = daily.loc[:, "1. open": "4. close"]
	df = pd.concat([price, ema, macd, fi.rename("FI"), fi_ema.rename("FI_2EMA")], axis=1, join='inner')
	df = df.dropna(how='any')
	return df

