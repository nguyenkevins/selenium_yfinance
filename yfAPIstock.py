import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

URL = 'https://finance.yahoo.com/quote/'

# Get options for chrome and make it headless when testing
# with the console message interupting
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
#options.add_argument('headless')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

# Selenium Driver for Chrome
path = r'chromedriver'

# Open driver and go to the URL
driver.get(URL)

def customMessage(input):
    return input

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