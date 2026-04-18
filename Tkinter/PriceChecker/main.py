import os
import smtplib
from dotenv import load_dotenv
import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
    "Accept-Language": "en-US,en;q=0.9,la;q=0.8"
}
pot_url = "https://appbrewery.github.io/instant_pot/"
solar_panel_url = "https://www.amazon.com/dp/B0BG1K1BQ7"

response = requests.get(solar_panel_url, headers=headers)
print(response.content)
soup = BeautifulSoup(response.content, "html.parser")
print(f"statuscode:{response.status_code}")
print(soup.prettify())
load_dotenv()
price = soup.find("span",class_="a-offscreen")
print(f"price span :{price}")
# Remove the dollar sign using split
price_without_currency = price.split("$")[1]

# Convert to floating point number
price_as_float = float(price_without_currency)
print(price_as_float)
#
# price_span = soup.find('span',class_="reinventPricePriceToPayMargin")
# price_whole = price_span.find('span',class_="a-price-whole").get_text(strip=True)
# price_fraction = price_span.find('span',class_="a-price-fraction").get_text(strip=True)
# #price_without_currency = price.split("$")[1]
#
# price_without_currency = price_whole +"."+price_fraction
#
# print(f"**********************\n{price_without_currency}\n*******************************")
# price_in_float = float(price_without_currency)
# print(f"price of the pot :{price_in_float}")

if price_as_float < 700.00:
    smtp = smtplib.SMTP(os.getenv("SMTP_ADDRESS"),port=587)
    smtp.starttls()
    smtp.login(user=os.getenv("EMAIL_ADDRESS"), password=os.getenv("EMAIL_PASSWORD"))
    smtp.sendmail(from_addr=os.getenv("EMAIL_ADDRESS"),
                          to_addrs="hpaks23@gmail.com",msg=f"Subject:Price Checker\n\nItem you wanted is priced below or at your asking price: {price_as_float}. But it at {solar_panel_url}")
