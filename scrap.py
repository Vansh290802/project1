from selenium import webdriver
from bs4 import BeautifulSoup
import pandas as pd
import requests
import time

letterss = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
name = []

for i in letterss:
        for k in range(1,38):
            URL = "https://www.wsj.com/market-data/quotes/company-list/a-z/" + i +"/" + str(k)
            headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
            page = requests.get(URL, headers=headers)
            if page.status_code == 200:
                    soup = BeautifulSoup(page.content, "html.parser")
                    table=soup.findAll("table", attrs={'class':'cl-table'})
                    df = pd.read_html(str(table))[0]
                    name.append([x for x in df['Name'])

print(name)
