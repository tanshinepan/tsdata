## tsdata

### Preparation

1. Get the API Key from [Alpha Vantage](https://www.alphavantage.co/)
2. `pip install tsdata`



### Scenario

Produce the JSON data of Microsoft Corporation (symbol: MSFT) or other symbol for first screen. 

```bash
tsdata produce MSFT --screen 1 --key <API Key>
```

Afterwards, you'll get the JSON data.

Drop it inside the dotted section of [TS website](https://tripe-screen-trading-system.web.app/) correctly.