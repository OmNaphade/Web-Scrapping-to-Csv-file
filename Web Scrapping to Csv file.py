from bs4 import BeautifulSoup
import requests
from csv import writer

url = r"https://zeplin.io/pricing/"
header = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                        "Chrome/109.0.0.0 Safari/537.36"}
r = requests.get(url, headers=header)
soup = BeautifulSoup(r.content, 'html.parser')
soup1 = BeautifulSoup(soup.prettify(), 'html.parser')
results = soup1.find_all('div', class_="zp-flex zp-flex-col zp-items-center")

plan_amount = ''

with open('data.csv', 'w', newline='', encoding='utf8') as f:
    thewriter = writer(f)
    header = ['Features', 'Plan_amount', 'is_Present']
    thewriter.writerow(header)

    for result in results:
        plan_amount1 = result.find('div', class_="zp-text-36 zp-leading-42 zp-font-light zp-text-gray-teflon zp-mr-12")
        if plan_amount1:
            plan_amount = plan_amount1.text.replace('\n', '')
        else:
            plan_amount = "Not mentioned!"
        features = result.find('ul').text.replace('\n', '')

        if plan_amount1:
            is_present = True
        else:
            is_present = False

        info = [features, plan_amount, is_present]
        thewriter.writerow(info)
