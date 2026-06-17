import requests
from bs4 import BeautifulSoup
import json

# Парсим свежие объявления
url = "https://www.olx.kz/zhambylskaya-oblast/q/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

ads = []
for item in soup.select('[data-cy="l-card"]'):
    try:
        title = item.select_one('h6').text.strip()
        price = item.select_one('[data-testid="ad-price"]').text.strip()
        ads.append({"title": title, "price": price})
    except: continue

# Сохраняем в файл, который будет читать сайт
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ads, f, ensure_ascii=False)
print("Тест прошел").
