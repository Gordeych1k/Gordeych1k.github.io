import requests
from bs4 import BeautifulSoup

def get_fuel_price():
    response = requests.get('https://index.minfin.com.ua/ua/markets/fuel/')
    soup = BeautifulSoup(response.text, 'html.parser')
    table = soup.find('table', class_='line')
    row = table.find_all('tr')[1].find_all("td")
    name = row[0].text
    price = row[2].text
    price_change = row[3].text
    procent_change = row[4].text
    return name, price, price_change, procent_change

if __name__ == '__main__' :
    data = get_fuel_price()
    print(data)
