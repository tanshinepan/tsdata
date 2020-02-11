import click
import tsdata
import logging
import boto3
from botocore.exceptions import ClientError
from io import StringIO 

def upload_fileobj(buf, object_name):
    bucket='triple-screen-data'
    s3_resource = boto3.resource('s3')
    response = s3_resource.Object(bucket, object_name).put(Body=buf.getvalue())

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
    buf = StringIO()
    if timeseries == 'daily':
        daily_df = tsdata.produce_daily(ticker)
        daily_df.to_json(buf, orient='index')
    elif timeseries == 'weekly':
        weekly_df = tsdata.produce_weekly(ticker)
        weekly_df.to_json(buf, orient='index')
    else:
        pass
    upload_fileobj(buf, object_name='{0}_{1}.json'.format(ticker, timeseries))

