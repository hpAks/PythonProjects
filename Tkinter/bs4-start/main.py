from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page,"html.parser")
main_table = soup.find(name="table", id="hnmain")
big_box = main_table.find(name="tr", id="bigbox")
title_box = big_box.select_one(selector="span.titleline")
title_one = title_box.find(name="a")
print(title_one.getText())

