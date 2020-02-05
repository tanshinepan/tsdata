import tsdata
import pandas as pd

def test_calculate_fi_ema():
		daily = pd.read_pickle(r'daily.pkl')
		fi, fi_ema = tsdata.calculate_fi(df=daily)

