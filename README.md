# Yahoo Finance API

![Demo1](https://github.com/nguyenkevins/win_api_yfinance/blob/master/stock1.png)

### Currently in-progress / 70% Completion
### In-Progress: Handshake Failure, Market Cap, PE Ratio, Dividend, and Ex-Dividend Function

## Summary
A python API that allow user to use the functions and apply it to their own code. With the carefully placed designs and efficient coding, the API maximizes simplicity for ease of use.

## Function Example
```python
yfAPIstock.priceStatus("T") # Prints out the price status

print(yfAPIstock.currentPrice("T")) # Returns a float for current price

print(yfAPIstock.netPrice("T")) # Returns a float for net price

print(yfAPIstock.netPercent("T")) # Returns a float for net percent price

print(yfAPIstock.previousPrice("T")) # Returns a float for previous price

print(yfAPIstock.openPrice("T")) # Retuns a float for open price

yfAPIstock.bidStatus("T") # Prints out the bid status

yfAPIstock.askStatus("T") # Prints out the ask status

yfAPIstock.dayRangeStatus("T") # Prints out day range status

yfAPIstock.yearRangeStatus("T") # Prints out year range status

print(yfAPIstock.currentVolume("T")) # Retuns a float for current volume

print(yfAPIstock.bidPrice("T")) # Returns a float for bid price

print(yfAPIstock.askPrice("T")) # Returns a float for ask price

print(yfAPIstock.averageVolume("T")) # Returns a float for averageVolume
```

## Prerequisites
* This project requires Python 3.5+
* Selenium Python Module and Selenium Driver (depending on OS)
* BeautifulSoup Python Module
