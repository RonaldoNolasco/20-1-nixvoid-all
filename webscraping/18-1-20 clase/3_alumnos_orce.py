import requests as r
from bs4 import BeautifulSoup

# 4 kind of objects Tag, NavigableString, BeautifulSoup, and Comment
url = "https://www.orce.uni.edu.pe/detaalu.php?id=20131169C&op=detalu"

# . <- navigable object

response = r.get(url, verify=False)
response.encoding = 'utf-8'
soup = BeautifulSoup(response.text, 'html.parser')
# print(soup.prettify())

# contents

#print(soup.table.tbody)
print("--------------------------------------------")
#print(soup.tbody)
#print("THEY'RE THE SAME")

#print(soup.tbody.find_all('tr'))
for x in soup.tbody.find_all('tr')[3:10]:
  tds = x.find_all('td')
  if len(tds)>1:
    print(tds[1].string)