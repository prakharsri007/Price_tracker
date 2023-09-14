import os  # Import the os module to access environment variables
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Get the PORT environment variable or use a default port (e.g., 8000)
PORT = int(os.environ.get("PORT", 8000))

URL = 'https://www.amazon.in/Acer-Predator-Processor-Windows-PHN16-71/dp/B0BYN3FGHR/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=Gkd65&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=1JA6RQN04BVCV9CQQ789&pd_rd_wg=fDXOS&pd_rd_r=9bb90039-2259-4aa3-b23e-720a5e7c9695&pd_rd_i=B0BYN3FGHR'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

while True:
    def check_price():
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')
        title = soup.find(id="productTitle").get_text()
        price = soup.find('span', {'class': 'a-price-whole'})
        price_text = price.get_text().replace(',', '').replace('.', '')
        price = int(price_text)
        print(price)
        print(title.strip())

        # this is the price check condition
        if price > 12000:
            send_mail()

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('007.praks007@gmail.com', 'csmx cyoi svdu bhwq')

        subject = 'Price Drop !!!!!!!'
        body = 'Check the Link Now!!! https://www.amazon.in/Acer-Predator-Processor-Windows-PHN16-71/dp/B0BYN3FGHR/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=Gkd65&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=1JA6RQN04BVCV9CQQ789&pd_rd_wg=fDXOS&pd_rd_r=9bb90039-2259-4aa3-b23e-720a5e7c9695&pd_rd_i=B0BYN3FGHR'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            '007.praks007@gmail.com',
            '1976.prakhar@gmail.com',
            msg
        )
        print('EMAILS ALERTS SENT')

        server.quit()

    check_price()
    time.sleep(12 * 60 * 60)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)  # Start the app with the specified PORT
