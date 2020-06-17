import os
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import csv

URL = 'https://finance.yahoo.com/gainers/?offset=0&count=200'

# Get options for chrome and make it headless when testing
# with the console message interupting
options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
options.add_argument('headless')

# initialize the driver
driver = webdriver.Chrome(chrome_options=options)

# Selenium Driver for Chrome
path = r'chromedriver'

# Open driver and go to the URL
driver.get(URL)

#print(driver.find_element_by_xpath("//tbody[@data-reactid='72']"))
html = driver.page_source
soup = BeautifulSoup(html, 'html.parser')
results = soup.find(id="fin-scr-res-table")



# Print out all available jobs from the scraped webpage
stock_elems = results.find_all("tr", class_="simpTblRow")
print()

with open('StockTopGainer.csv', mode='w', newline='') as stockgainer_file:
    stockgainer_writer = csv.writer(stockgainer_file, skipinitialspace=True, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    stockgainer_writer.writerow(["NAME", "SYMBOL", "PRICE", "CHANGE", "CHANGE%", "VOL", "VOL3MO", "M.CAP", " ", " ", "(TOP", "STOCK", "GAINER", "TODAY)"])
    for stock_elem in stock_elems:
        name = stock_elem.find("td", class_="Va(m) Ta(start) Px(10px) Fz(s)")
        symbol = stock_elem.find("a")
        price = stock_elem.find("span", class_="Trsdu(0.3s)")
        change = stock_elem.find("span", class_="Trsdu(0.3s) Fw(600) C($positiveColor)" )
        volume = stock_elem.find("td", class_="Va(m) Ta(end) Pstart(20px) Fz(s)")
        vol3 = stock_elem.find('td', {'aria-label': 'Avg Vol (3 month)'})
        mcap = stock_elem.find("td", class_="Va(m) Ta(end) Pstart(20px) Pend(10px) W(120px) Fz(s)")
        if None in (name, symbol, price, change, volume, vol3, mcap):
            continue
        print("Name:     ", name.text.strip())
        print("Symbol:   ", symbol.text.strip())
        print("Price:    ", price.text.strip())
        print("Change:   ", change.text.strip())
        print("Change %: ", round((1-(float(price.text.strip().replace(',', ''))/(float(price.text.strip().replace(',', ''))-float(change.text.strip()))))*100*(-1), 2))
        print("Volume:   ", volume.text.strip())
        print("VOL 3mo:  ", vol3.text.strip())
        print("M.Cap:    ", mcap.text.strip())
        print()
        stockgainer_writer.writerow([name.text.strip(), symbol.text.strip(), price.text.strip(), change.text.strip(), round((1-(float(price.text.strip().replace(',', ''))/(float(price.text.strip().replace(',', ''))-float(change.text.strip()))))*100*(-1), 2), volume.text.strip(), vol3.text.strip(), mcap.text.strip()])

driver.close()
driver.quit()
#os.system("pause")
