import requests
from bs4 import BeautifulSoup

# URL національного банку для отримання курсів валют
url = 'https://bank.gov.ua/en/markets/exchangerates'  # Замініть це на URL свого національного банку

# Відправляємо GET-запит до сайту національного банку
response = requests.get(url)
# print(response.text)

# Перевіряємо, чи отримано успішну відповідь
if response.status_code == 200:
    # Отримуємо HTML-код відповіді
    html = response.text

    # Парсимо HTML-код з використанням BeautifulSoup
    soup = BeautifulSoup(html, 'html.parser')

    # Знаходимо елементи з курсами валют та витягуємо інформацію
    # currency_elements = soup.find_all('span', class_='currency')  # Замініть це на відповідні CSS-класи на вашому сайті
    # exchange_rate_elements = soup.find_all('span', class_='exchange-rate')  # Замініть це на відповідні CSS-класи на вашому сайті

    currency_elements = soup.find_all("td", {"data-label": "Letter code"})
    currency_full_name = soup.find_all("td", {"data-label": "Currency name"})
    exchange_rate_elements = soup.find_all("td", {"data-label": "UAH"})

    # print(currency_elements)
    # print(exchange_rate_elements)
    # Виводимо на екран курси валют
    for i in range(len(currency_elements)):
        currency = currency_elements[i].text.strip()
        currency_name = currency_full_name[i].text.strip()
        exchange_rate = exchange_rate_elements[i].text.strip()
        print(f'Валюта: {currency_name}({currency}), Курс: {exchange_rate}')
else:
    print('Помилка отримання відповіді від сервера')