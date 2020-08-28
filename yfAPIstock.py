import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv
import logging
from selenium.webdriver.remote.remote_connection import LOGGER

URL = 'https://finance.yahoo.com/quote/'

# Get options for chrome and make it headless when testing
# with the console message interupting
options = webdriver.ChromeOptions()
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)
options.add_argument('log-level=3')
options.add_argument('--ignore-certificate-errors-spki-list')
options.add_argument('--ignore-ssl-errors')
options.add_argument('headless')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

# Selenium Driver for Chrome
path = r'chromedriver'

def customMessage(input):
    return input

def priceStatus(symbol):
    # Default price value to -1
    price = -1
    price2 = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    if(stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
        price2 = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
    else:
        price2 = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")

    print("Price of " + symbol + " is: $" + price.text.strip() + "   $" + price2.text.strip())


def currentPrice(symbol):
    # Default price value to -1
    price = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")
    return float(price.text.strip())

def netPrice(symbol):
        # Default price value to -1
    price = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    if(stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
    else:
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")

    return float(price.text.strip().split()[0])

def netPercent(symbol):
    # Default price value to -1
    price = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="Lead-3-QuoteHeader-Proxy")
    stock_elems = results.find("div", class_="D(ib) Mend(20px)")
    if(stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")):
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($positiveColor)")
    else:
        price = stock_elems.find("span", class_="Trsdu(0.3s) Fw(500) Pstart(10px) Fz(24px) C($negativeColor)")
        
    return float(price.text.strip().split()[1].replace('(', '').replace(')', '').replace('%', ''))/100.0

def previousPrice(symbol):
    # Default price value to -1
    pprice = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")
    pprice = results.find('span', {'data-reactid': '98'})
    return float(pprice.text.strip())

def openPrice(symbol):
    # Default price value to -1
    oprice = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")
    oprice = results.find('span', {'data-reactid': '103'})
    return float(oprice.text.strip())

def bidStatus(symbol):
    # Default price value to -1
    bStatus = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('span', {'data-reactid': '108'})):
        bStatus = results.find('span', {'data-reactid': '108'})
    else:
        bStatus = results.find('td', {'data-reactid': '107'})
    print(bStatus.text.strip())

def bidPrice(symbol):
    # Default price value to -1
    bPrice = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('span', {'data-reactid': '108'})):
        bPrice = results.find('span', {'data-reactid': '108'})
    else:
        bPrice = results.find('span', {'data-reactid': '108'})
    if bPrice is not None:
        bPrice = bPrice.text.strip()
        return float(bPrice.split(' x ')[0])
    else:
        return float(0)



def askStatus(symbol):
    # Default price value to -1
    aStatus = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'ASK-value'})):
        aStatus = results.find('td', {'data-test': 'ASK-value'})
    else:
        aStatus = results.find('td', {'data-reactid': '113'})
    print(aStatus.text.strip())

def askPrice(symbol):
    # Default price value to -1
    aPrice = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'ASK-value'})):
        aPrice = results.find('td', {'data-test': 'ASK-value'})
    else:
        aPrice = results.find('td', {'data-reactid': '113'})

    if aPrice is not None:
        aPrice = aPrice.text.strip()
        return float(aPrice.split(' x ')[0])
    else:
        return float(0)

def dayRangeStatus(symbol):
    # Default price value to -1
    dRStatus = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'DAYS_RANGE-value'})):
        dRStatus = results.find('td', {'data-test': 'DAYS_RANGE-value'})
    else:
        dRStatus = results.find('td', {'data-reactid': '117'})
    print(dRStatus.text.strip())

def yearRangeStatus(symbol):
    # Default price value to -1
    dRStatus = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})):
        dRStatus = results.find('td', {'data-test': 'FIFTY_TWO_WK_RANGE-value'})
    else:
        dRStatus = results.find('td', {'data-reactid': '117'})
    print(dRStatus.text.strip())

def currentVolume(symbol):
    # Default price value to -1
    cVolume = -1
    
    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'TD_VOLUME-value'})):
        cVolume = results.find('td', {'data-test': 'TD_VOLUME-value'})
    else:
        cVolume = results.find('td', {'data-reactid': '125'})
    return float(cVolume.text.strip().replace(',', ''))

def averageVolume(symbol):
    # Default price value to -1
    aVolume = -1

    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")

    if(results.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'})):
        aVolume = results.find('td', {'data-test': 'AVERAGE_VOLUME_3MONTH-value'})
    else:
        aVolume = results.find('td', {'data-reactid': '129'})
    return float(aVolume.text.strip().replace(',', ''))

def marketCap(symbol):
    # Default price value to -1
    mCap = -1

    # Open driver and go to the URL
    newURL = URL + symbol + "?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")
    stock_elems = results.find("td", class_="Ta(end) Fw(600) Lh(14px)")
    price = stock_elems.find('td', {'data-reactid': '136'})
    return price

def peRatio(symbol):
    # Default price value to -1
    pe = -1

    # Open driver and go to the URL
    newURL = URL + symbol +"?p=" + symbol

    driver.get(newURL)
    html = driver.page_source
    soup = BeautifulSoup(html, 'html.parser')

    results = soup.find(id="quote-summary")


    pe = results.find('span', {'data-reactid': '147'})
    print(pe)
    return 0