from bs4 import BeautifulSoup

with open("Python-Basic/Data Scraping/nation_temp.html","r") as f:
    html_doc = f.read()

soup = BeautifulSoup(html_doc,'html.parser')
# print(soup.prettify()) 
# print(soup.title)
# print(soup.title.string)
# print(soup.div)
# print(soup.find_all("div"))

# for link in soup.find_all("a"):
#     print(link.get("href"))

# print(soup.find_all(class_="row")

# for row in soup.find_all(class_="row"):
#     print(row,"\n")

# print(soup.find(id="theme-data"))
# print(soup.select("div.row"))
# print(soup.select("div#skeleton"))
# print(soup.select("span.spinner__circle"))
# print(soup.find("span"))
# print(soup.span.get("class"))

# for child in soup.find(class_="notion-body").children:
#     print(child)

# for parent in soup.find(class_="spinner").parent:
#     print(parent)

# cont = soup.find(class_="row")
# cont["class"] = "my_row"
# print(cont)

cont = soup.find(id="skeleton")
print(cont.has_attr("role"))