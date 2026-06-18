import requests
from bs4 import BeautifulSoup
import json

# Заголовки для имитации реального браузера
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36'
}

url = "https://krisha.kz/arenda/kvartiry/zhambylskaya-oblast/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

ads = []
# Ищем все карточки объявлений
items = soup.find_all('div', class_='a-card')

for item in items:
    try:
        # Название
        title_tag = item.select_one('.a-card__title')
        title = title_tag.text.strip() if title_tag else "Без названия"
        
        # Цена
        price_tag = item.select_one('.a-card__price')
        price = price_tag.text.strip() if price_tag else "Цена не указана"
        
        # Фото (самое важное: ищем data-src или src)
        img_tag = item.find('img', class_='a-card__image-picture')
        if img_tag:
            # Сначала проверяем data-src, если нет — берем src
            img_url = img_tag.get('data-src') or img_tag.get('src')
        else:
            img_url = "https://via.placeholder.com/200"
            
        ads.append({"title": title, "price": price, "img": img_url})
    except Exception as e:
        continue

# Сохраняем данные
with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ads, f, ensure_ascii=False)
