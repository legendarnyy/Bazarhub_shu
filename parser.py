import requests
from bs4 import BeautifulSoup
import json

# Меняем заголовки на "человеческие"
headers = {
    'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 15_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/15.0 Mobile/15E148 Safari/604.1'
}

url = "https://www.olx.kz/zhambylskaya-oblast/q/"
response = requests.get(url, headers=headers)
soup = BeautifulSoup(response.text, 'html.parser')

ads = []
# Ищем элементы карточек
items = soup.select('div[data-cy="l-card"]')

for item in items:
    try:
        title = item.select_one('h6').text.strip()
        price = item.select_one('p[data-testid="ad-price"]').text.strip()
        ads.append({"title": title, "price": price})
    except: continue

with open("data.json", "w", encoding="utf-8") as f:
    json.dump(ads, f, ensure_ascii=False)
