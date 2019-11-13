## tsdata

Produce json file for [TS website](https://tripe-screen-trading-system.web.app/).

![](./snapshots/website.png)

## Getting Started

### Prerequisites

Get the API Key from [Alpha Vantage](https://www.alphavantage.co/)

### Installing

`pip install tsdata`

### Running

Produce the data of Microsoft Corporation (symbol: MSFT) for first screen. 

```bash
tsdata produce MSFT --screen 1 --key <API Key>
```

Afterwards, you'll get *MSFT_first_screen.json*.



