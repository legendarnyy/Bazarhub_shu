import requests
from bs4 import BeautifulSoup
import json

# Запрос к странице
url = "https://www.olx.kz/zhambylskaya-oblast/q/"
headers = {'User-Agent': 'Mozilla/5.0'}
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

ads = []
# Ищем контейнеры с объявлениями - теперь пробуем более общий селектор
items = soup.find_all('div', {'data-cy': 'l-card'})

for item in items:
    try:
        title = item.find('h6').text.strip()
        # Ищем цену более надежным способом
        price_tag = item.find('p', {'data-testid': 'ad-price'})
        price = price_tag.text.strip() if price_tag else "Цена не указана"
        
        ads.append({"title": title, "price": price})
    except Exception as e:
        continue

# Сохраняем результат
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ads, f, ensure_ascii=False)
