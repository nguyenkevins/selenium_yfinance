# Yahoo Finance API

![Demo1](https://github.com/nguyenkevins/MinMusic/blob/master/app/src/main/res/picA.jpg)

### Currently in-progress / 70% Completion
### In-Progress: Market Cap, PE Ratio, Dividend, and Ex-Dividend Function

## Summary
A python API that allow user to use the functions and apply it to their own code. With the carefully placed designs and efficient coding, the API maximizes simplicity for ease of use.

## Example
```python
yfAPIstock.priceStatus("T")
print(yfAPIstock.currentPrice("T"))
print(yfAPIstock.netPrice("T"))
print(yfAPIstock.netPercent("T"))
print(yfAPIstock.previousPrice("T"))
print(yfAPIstock.openPrice("T"))
yfAPIstock.bidStatus("T")
yfAPIstock.askStatus("T")
yfAPIstock.dayRangeStatus("T")
yfAPIstock.yearRangeStatus("T")
print(yfAPIstock.currentVolume("T"))
print(yfAPIstock.bidPrice("T"))
print(yfAPIstock.askPrice("T"))
print(yfAPIstock.averageVolume("T"))
```

## Prerequisites
* This project requires Python 3.5+
* Selenium Python Module and Selenium Driver (depending on OS)
* BeautifulSoup Python Module
