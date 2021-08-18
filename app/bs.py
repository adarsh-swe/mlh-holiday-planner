import requests
from requests_html import HTMLSession
from bs4 import BeautifulSoup

url = 'https://www.skyscanner.ca/transport/flights/yyz/yyc/210822/210829'
# try: 
# 	session = HTMLSession()
# 	res = session.get(url)
# except requests.exceptions.RequestException as e: 
# 	print(e)

res = requests.get(url).text

print(res)