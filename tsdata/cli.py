import click
import tsdata

@click.group()
def cli():
	"""
		Hello! Welcome to use tsdata.
	"""
	pass

@cli.command()
@click.argument('ticker')
@click.option('--key', required=True,
		help="claim your API key from Alpha Vantage")
@click.option('--screen', default=1, show_default=True, type=int,
		help="first screen(1) or second screen(2)")
def produce(ticker, key, screen):
	"""
		Produce the JSON data for first screen and second screen.

		Ticker is the name of the equity of your choice.
		For example, "MSFT" represents Microsoft Corporation.
		If the ticker is not U.S. stock, try to append the exchange code.
		For example, "2330:TW" represents TSMC located in Taiwan.
	"""
	tsdata.init(key)
	with click.progressbar(length=4) as bar:
		def updateProgreeBar():
			bar.update(1)
		if (screen == 2):
			tsdata.produce_the_second(ticker, updateProgreeBar)
		else:
			tsdata.produce_the_first(ticker, updateProgreeBar)

