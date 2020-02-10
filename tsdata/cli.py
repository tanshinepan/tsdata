import click
import tsdata

@click.command()
@click.argument('ticker')
@click.option('-t','--timeseries',required=True,type=click.Choice(['daily', 'weekly']))
def cli(ticker, timeseries):
	"""
		Ticker is the name of the equity of your choice.
		For example, "MSFT" represents Microsoft Corporation.
		If the ticker is not U.S. stock, try to append the exchange code.
		For example, "2330:TW" represents TSMC located in Taiwan.
	"""
	if timeseries == 'daily':
		daily_df = tsdata.produce_daily(ticker)
		daily_df.to_json(r'{}_daily.json'.format(ticker), orient='index')
	elif timeseries == 'weekly':
		weekly_df = tsdata.produce_weekly(ticker)
		weekly_df.to_json(r'{}_weekly.json'.format(ticker), orient='index')
	else:
		pass
