import requests
from bs4 import BeautifulSoup

iamhuman = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36"
}

URL = "https://www.melon.com/chart/day/index.htm"
result = requests.get(URL, headers=iamhuman)
soup = BeautifulSoup(result.text, "html.parser")

songs = soup.find_all("div", {"class": "ellipsis rank01"})

for i in songs:
    print(i.find("a").text)
