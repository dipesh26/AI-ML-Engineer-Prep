import requests

def data_fetching(url, path):
    r = requests.get(url)
    with open(path, "w") as f:
        f.write(r.text)

url = "https://www.notion.so/20e40b3dadee80f2a366edebd1a8e135?v=20e40b3dadee8022b6a3000c6165c703"    
data_fetching(url, "nation_temp.html")