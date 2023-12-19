import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL ='https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_4?crid=3HD6EHRJKTY2K&keywords=sony%2Ba7&qid=1702772332&sprefix=sony%2Ba7%2Caps%2C144&sr=8-4&th=1'

headers = {
    "User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'}
def check_price():
    page = requests.get(URL, headers = headers)

    soup = BeautifulSoup(page.content, 'html.parser')


    title = soup.find(id="productTitle").get_text()
    price = soup.find(id="priceblock_ourprice").get_text()
    coverted_price = float(price[0:5])

    if(converted_price < 1.700):
        send_mail()
    print(converted_price)
    print(title.strip())
    if(converted_price>1.700):
        send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()


    server.login('ed.magician@gmail.com', 'mjutimzlroarivxo')

    subject  = 'Price fell down!'
    body = 'https://www.amazon.com/Sony-Full-Frame-Mirrorless-Interchangeable-Lens-ILCE7M3/dp/B07B43WPVK/ref=sr_1_4?crid=3HD6EHRJKTY2K&keywords=sony%2Ba7&qid=1702772332&sprefix=sony%2Ba7%2Caps%2C144&sr=8-4&th=1'

    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'ed.magician@gmail.com',
        'simo.edwin@yahoo.com',
        msg

    )

print('HEY EMAIL HAS BEEN SENT!')

server.quit()

while(True):
    check_price()
    time.sleep(60 * 60)