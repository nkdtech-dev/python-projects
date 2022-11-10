import requests
from bs4 import BeautifulSoup

from twilio.rest import Client

TWILIO_SID = "AC4d924864212383a8ddb4499b43aef02f"
TWILIO_AUTH_TOKEN = "9a85308656609209d532ac1f0ecd33ab"
TWILIO_VIRTUAL_NUMBER = "+12135893147"
TWILIO_VERIFIED_NUMBER = "+237672944309"
client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)
TARGET_PRICE = 100

amozon_watch_url = "https://www.amazon.com/dp/B07TYNMRZG/ref=va_live_carousel?pf_rd_r=9NSBZA102DS6EKZ08WTE&pf_rd_" \
                   "p=93a12f85-1a5e-426c-9596-f07ee890efcf&pf_rd_m=ATVPDKIKX0DER&pf_rd_t=HighVelocityEvent&pf_rd_i=" \
                   "deals_1_desktop&pf_rd_s=slot-13&linkCode=ilv&tag=swiftwellness-20&ascsubtag=MORE_GIFT_IDEAS_Black" \
                   "_Friday_Deals_221109215506&asc_contentid=amzn1.amazonlive.broadcast.4e662f79-9c62-45ba-b0d9-053fa" \
                   "87dc996&pd_rd_i=B07TYNMRZG&th=1&psc=1"
header_elm = {
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 "
                  "Safari/537.36",
    "Accepted-Language": "en-Gb,en-Us;q=0.9,en;q=0.8"
}
response = requests.get(url=amozon_watch_url, headers=header_elm)
data = response.text
soup = BeautifulSoup(data, "lxml")
item_price = soup.find("span", class_="a-offscreen").text
current_price = float(item_price.split('$')[1])
item_name=soup.find("span", class_="a-size-large product-title-word-break").text
if current_price <= TARGET_PRICE:
    message = client.messages.create(
        body=f"the {item_name} \n is now💵💰${current_price}. below your target price. 🅱️uy now",
        from_=TWILIO_VIRTUAL_NUMBER,
        to=TWILIO_VERIFIED_NUMBER
    )
else:
    print("price is still too high")