import request
from bs4 import BeautifulSoup

URL = "https://www.amazon.com/Echo-Dot/dp/B07FZ8S74R/ref=sr_1_1?crid=1RG8TKOBLJE94&keywords=echo+dot&qid=1563810895&s=gateway&sprefix=ech%2Caps%2C187&sr=8-1"

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/75.0.3770.142 Safari/537.36'}

page = request.get(URL, headers=header)

soup = BeautifulSoup(page.content, 'html.paser')

title = soup.find(id="productTitle").get_text()

print(title)
