import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL= 'https://www.amazon.in/LG-Ultragear-Compatible-Monitor-Display/dp/B08J5YGC9V/?_encoding=UTF8&pd_rd_w=5cuok&content-id=amzn1.sym.e5c03be3-10ba-4bc8-b9be-6fcea12320ed%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=e5c03be3-10ba-4bc8-b9be-6fcea12320ed&pf_rd_r=KV326X8FFHJY42ZCA71Q&pd_rd_wg=DFgLM&pd_rd_r=feae59b1-38ae-4f57-8c66-2cebf863fb7e&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/116.0.0.0 Safari/537.36'}
while True:
    def check_price():
        page= requests.get(URL , headers=headers)
        soup= BeautifulSoup(page.content, 'html.parser')
        title= soup.find(id="productTitle").get_text()
        price= soup.find('span', {'class': 'a-price-whole'})
        price_text = price.get_text().replace(',', '').replace('.', '')
        price=int(price_text)
        print(price)
        print(title.strip())

        #this is the price check condition
        if(price <= 12000):
            send_mail()
    

    def send_mail():
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login('007.praks007@gmail.com' , 'csmx cyoi svdu bhwq')

        subject = 'Price Drop !!!!!!!'
        body= 'Check the Link Now!!! https://www.amazon.in/LG-Ultragear-Compatible-Monitor-Display/dp/B08J5YGC9V/?_encoding=UTF8&pd_rd_w=5cuok&content-id=amzn1.sym.e5c03be3-10ba-4bc8-b9be-6fcea12320ed%3Aamzn1.symc.adba8a53-36db-43df-a081-77d28e1b71e6&pf_rd_p=e5c03be3-10ba-4bc8-b9be-6fcea12320ed&pf_rd_r=KV326X8FFHJY42ZCA71Q&pd_rd_wg=DFgLM&pd_rd_r=feae59b1-38ae-4f57-8c66-2cebf863fb7e&ref_=pd_gw_ci_mcx_mr_hp_atf_m&th=1'

        msg = f"Subject: {subject}\n\n{body}"

        server.sendmail(
            '007.praks007@gmail.com',
            '1976.prakhar@gmail.com',
            msg
        )
        print('EMAILS ALERTS SENT')

        server.quit()
    time.sleep(60*60)   
    check_price()    