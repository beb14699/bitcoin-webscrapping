from urllib.request import urlopen as req
from bs4 import BeautifulSoup as source

webURL = 'https://coinmarketcap.com/th/currencies/bitcoin/'

webopen = req(webURL)
page_html = webopen.read()
webopen.close()

data = source(page_html, 'html.parser')

temp = data.findAll ('div', { 'class' : 'priceValue___11gHJ' })
print(temp [0] . text)

