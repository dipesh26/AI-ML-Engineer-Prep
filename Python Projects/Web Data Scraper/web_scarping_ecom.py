import requests
from bs4 import BeautifulSoup
import pandas as pd

data = {"Title" : [], "Price" : [], "Stock" : []}

url = "https://books.toscrape.com/"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}

r = requests.get(url, headers=headers)

soup = BeautifulSoup(r.text, 'html.parser')
# print(soup.prettify())

books = soup.find_all('article', class_="product_pod")

for book in books:
    title = book.h3.a["title"]
    price = book.find('p', class_="price_color").text
    data["Title"].append(title)
    data["Price"].append(price)

print(data)


df = pd.DataFrame.from_dict(data)
df.to_csv("practice-book-data.csv", index=False)