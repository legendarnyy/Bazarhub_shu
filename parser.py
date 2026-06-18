# ... внутри цикла for item in items:
    try:
        title = item.select_one('.a-card__title').text.strip()
        price = item.select_one('.a-card__price').text.strip()
        # Добавляем получение ссылки на фото
        img_tag = item.select_one('img')
        img_url = img_tag['data-src'] if img_tag and 'data-src' in img_tag.attrs else (img_tag['src'] if img_tag else "https://via.placeholder.com/200")
        
        ads.append({"title": title, "price": price, "img": img_url})
    except: continue
# ...
