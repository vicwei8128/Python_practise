from bs4 import BeautifulSoup

with open("table.html", "r", encoding="UTF-8") as fp:
    soup = BeautifulSoup(fp, "html.parser")

friends = []
trs = soup.select("tr")
# 第一個<tr>的index為0，儲存的是標題不是資料內容，所以從index為1開始取值
for i in range(1, len(trs)):
    tr = trs[i]
    friend = []
    for td in tr.select("td"):
        friend.append(td.text.strip())
    friends.append(friend)

print(friends)