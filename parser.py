name: Обновление товаров
on:
  schedule:
    - cron: '0 * * * *' # Запускать каждый час
  workflow_dispatch:    # Кнопка «Запустить сейчас»

jobs:
  update:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - name: Установка Python
        uses: actions/setup-python@v4
        with: {python-version: '3.9'}
      - name: Установка библиотек
        run: pip install requests beautifulsoup4
      - name: Запуск робота
        run: python parser.py
      - name: Сохранение изменений
        run: |
          git config --global user.name 'Bot'
          git config --global user.email 'bot@email.com'
          git add data.json
          git commit -m 'Обновил товары' || exit 0
          git push
