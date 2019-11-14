## TSdata
Produce data for [TS website](https://tripe-screen-trading-system.web.app/). 

![](./snapshots/website.png)

### Prerequisites

- Get the <API Key> from [Alpha Vantage](https://www.alphavantage.co/)
- Install packages from [PyPI](https://pypi.org/).

### Full example

```sh
$ pip install tsdata
$ tsdata produce --help
// Produce data of Microsoft Corporation (symbol: MSFT) for first screen.
$ tsdata produce MSFT --screen 1 --key <API Key>
```

