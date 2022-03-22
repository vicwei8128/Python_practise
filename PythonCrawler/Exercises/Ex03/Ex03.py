import requests
from bs4 import BeautifulSoup

url = "https://www.tenlong.com.tw/search?availability=buyable&display=list&keyword=python&langs%5B%5D=all"
headers = {
    "user-agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36"}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, "html.parser")
# <div class="book-data">內有書的資訊
for div in soup.select("div.book-data"):
    # 取得書名
    name = div.a.text.strip()
    # 取得出版日期
    publishDate = div.select_one("span.publish-date").text.strip()
    # 取得定價
    price = div.select_one("span.price").text.strip()
    print(f"{price}\t{publishDate}\t{name}")

