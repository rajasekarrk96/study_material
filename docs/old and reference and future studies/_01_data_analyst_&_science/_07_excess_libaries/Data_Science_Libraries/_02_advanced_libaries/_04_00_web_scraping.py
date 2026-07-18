# pipenv install beautifulsoup4
# pipenv install requests
import requests
from bs4 import BeautifulSoup
response=requests.get("https://www.eduspheresolutions.com")
soup=BeautifulSoup(response.text,"html.parser")
ele=soup.select("title")
# l=soup.find_all("div",{"class":"container"})
l=soup.select("div",{"class":"container"})
print(l[0].text,l)
# print(type(ele))
print(ele[0].attrs)#attributes
print(ele[0].text)#text inside it