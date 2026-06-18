import requests
from bs4 import BeautifulSoup
import json

# Заголовки для имитации браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36'
}

# Пример: парсим квартиры в аренду в Жамбылской области
url = "https://krisha.kz/arenda/kvartiry/zhambylskaya-oblast/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

ads = []
# На Krisha.kz карточки обычно лежат в блоках с этим классом
items = soup.select('.a-card')

for item in items:
    try:
        title = item.select_one('.a-card__title').text.strip()
        price = item.select_one('.a-card__price').text.strip()
        ads.append({"title": title, "price": price})
    except: continue

# Сохраняем результат
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ads, f, ensure_ascii=False)
