from bs4 import BeautifulSoup
import requests

url = "https://www.washingtonpost.com/technology/2020/09/25/privacy-check-blacklight/" 
response = requests.get(url)
w_webpage = response.text

soup = BeautifulSoup(w_webpage, "html.parser")

title = soup.find(name="title")
print(title.text)

article_title = soup.find(name="span", class_="PJLV")
print(article_title.text)

byline = soup.find(name="a", rel="author", class_="wpds-c-cNdzuP wpds-c-cNdzuP-ejzZdU-isLink-true")
print(byline.text)

updated_date = soup.find(name="span", class_="wpds-c-iKQyrV")
print(updated_date.text)

content = soup.find_all(name="p", class_="wpds-c-cYdRxM wpds-c-cYdRxM-iPJLV-css overrideStyles font-copy", dir="null")
for para in content:
    print(para.getText())







