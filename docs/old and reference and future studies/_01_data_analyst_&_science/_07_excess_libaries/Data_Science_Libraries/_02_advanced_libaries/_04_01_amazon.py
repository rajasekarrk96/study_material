# pipenv install beautifulsoup4
# pipenv install requests
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.flipkart.com/search?q=mobiles&sid=tyy%2C4io&as=on&as-show=on&otracker=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_4_na_na_na&as-pos=1&as-type=RECENT&suggestionId=mobiles%7CMobiles&requestId=3d740225-c064-445b-8209-5711ce2bf439&as-backfill=on")
soup=BeautifulSoup(response.text,"html.parser")
# ele=soup.select("title")
# print(type(ele))
# print(soup.text)
# fin=soup.find_all("div",{"class":"_4rR01T"})
# price=soup.find_all("div",{"class":"_30jeq3 _1_WHN1"})
# for x in fin:
#     print(x.text)
# for x in price:
#     print(x.text)
# # print(ele[0].attrs)#attributes
# print(ele[0].text)#text inside it
# for x in ele:
#     print(x.text)
na=[]
fin = soup.find_all("div", {"class": "_4rR01T"})
for k in fin:
    na.append(k.get_text())
pr = []
fin = soup.find_all("div", {"class": "_30jeq3"})
for k in fin:
    pr.append(k.get_text())

ra = []
fin = soup.find_all("div", {"class": "_3LWZlK"})
for k in fin:
    ra.append(k.get_text())

import xlsxwriter as x

w = x.Workbook("mobile.xlsx")
wb = w.add_worksheet()
wb.write(0, 0, "Mobile name")
wb.write(0, 1, "Price")
wb.write(0, 2, "Rating")
row = 1
col = 0
for k in zip(na, pr, ra):
    wb.write(row, col, k[0])
    wb.write(row, col + 1, k[1])
    wb.write(row, col + 2, k[2])
    row += 1
w.close()
import os

os.system("mobile.xlsx")