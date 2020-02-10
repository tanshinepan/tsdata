import tsdata
import pytest
import pandas as pd

@pytest.fixture
def extract_daily():
		# import pathlib
		# pickle_path = pathlib.PurePath(pathlib.Path(__file__).parent).joinpath('daily.pkl')
		from alpha_vantage.timeseries import TimeSeries
		AV_KEY = 'AMZN'
		ticker = 'AMZN'
		ts = TimeSeries(AV_KEY, output_format='pandas')
		return ts.get_daily_adjusted(symbol=ticker, outputsize='20')

# https://stackoverflow.com/a/3430395/5254013
def test_calculate_fi_ema(extract_daily):
		daily, daily_meta_data = extract_daily
		fi, fi_ema = tsdata.calculate_fi(df=daily)
		print(fi_ema)

