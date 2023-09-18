import os  # Import the os module to access environment variables
import requests
from bs4 import BeautifulSoup
import smtplib
import time

# Get the PORT environment variable or use a default port (e.g., 8000)
PORT = int(os.environ.get("PORT", 8000))

URL = 'https://www.amazon.in/LG-Ultragear-Native-Monitor-Freesync/dp/B08J5YGC9V/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=BFMxy&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=AG1YRNN81AN5R6RSK022&pd_rd_wg=7Nt8A&pd_rd_r=748e3919-ac6e-422b-8d06-dc75ac166cd3&pd_rd_i=B08J5YGC9V&th=1'

headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}

while True:
    def check_price():
        try:
            page = requests.get(URL, headers=headers)
            soup = BeautifulSoup(page.content, 'html.parser')
            title = soup.find(id="productTitle")
            price = soup.find('span', {'class': 'a-price-whole'})

            if title is not None:
                title_text = title.get_text().strip()
                print(title_text)
            else:
                print("Product title not found.")

            if price is not None:
                price_text = price.get_text().replace(',', '').replace('.', '')
                price = int(price_text)
                print(price)
            else:
                print("Product price not found.")

            # Check the price condition
            if price is not None and price > 12000:
                send_mail()
        except Exception as e:
            print("An error occurred:", str(e))

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('007.praks007@gmail.com', 'csmx cyoi svdu bhwq')

        subject = 'Price Drop !!!!!!!'
        body = 'Check the Link Now!!! https://www.amazon.in/LG-Ultragear-Native-Monitor-Freesync/dp/B08J5YGC9V/ref=pd_ci_mcx_mh_mcx_views_0?pd_rd_w=BFMxy&content-id=amzn1.sym.cd312cd6-6969-4220-8ac7-6dc7c0447352%3Aamzn1.symc.ca948091-a64d-450e-86d7-c161ca33337b&pf_rd_p=cd312cd6-6969-4220-8ac7-6dc7c0447352&pf_rd_r=AG1YRNN81AN5R6RSK022&pd_rd_wg=7Nt8A&pd_rd_r=748e3919-ac6e-422b-8d06-dc75ac166cd3&pd_rd_i=B08J5YGC9V&th=1'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            '007.praks007@gmail.com',
            '1976.prakhar@gmail.com',
            msg
        )
        print('EMAILS ALERTS SENT')

        server.quit()

    check_price()
    time.sleep(2 * 60)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=PORT)  # Start the app with the specified PORT
