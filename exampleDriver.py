import os
import yfAPIstock

print("")
print(yfAPIstock.customMessage("Interacting with yfAPIstock..."))
print("")

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
print(yfAPIstock.marketCap("T")) #Market Cap BUG!
print(yfAPIstock.peRatio("T")) #PE Ratio BUG!

yfAPIstock.priceStatus("AGNC")
print(yfAPIstock.currentPrice("AGNC"))
print(yfAPIstock.netPrice("AGNC"))
print(yfAPIstock.netPercent("AGNC"))
print(yfAPIstock.previousPrice("AGNC"))
print(yfAPIstock.openPrice("AGNC"))
yfAPIstock.bidStatus("AGNC")
yfAPIstock.askStatus("AGNC")
yfAPIstock.dayRangeStatus("AGNC")
yfAPIstock.yearRangeStatus("AGNC")
print(yfAPIstock.currentVolume("AGNC"))
print(yfAPIstock.bidPrice("AGNC"))
print(yfAPIstock.askPrice("AGNC"))
print(yfAPIstock.averageVolume("AGNC"))
print(yfAPIstock.marketCap("AGNC")) #Market Cap BUG!
print(yfAPIstock.peRatio("AGNC")) #PE Ratio BUG!