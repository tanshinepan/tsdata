import os
from alpha_vantage.techindicators import TechIndicators
from alpha_vantage.timeseries import TimeSeries

AV_KEY = os.getenv('AV_KEY')
ticker = 'AMZN'

ti = TechIndicators(AV_KEY, output_format='pandas')
ts = TimeSeries(AV_KEY, output_format='pandas')

daily, daily_meta_data = ts.get_daily_adjusted(symbol=ticker, outputsize='full')
daily.to_pickle(r'daily.pkl')

