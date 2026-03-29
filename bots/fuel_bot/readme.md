# бот-моніторинг паливо
## архітектура
сайт: index.minfin, https://index.minfin.com.ua/ua/markets/fuel/
пайтон: requests , beautifulsoup4

## файли
.env - для зберігання конфіденційних даних (токени, паролі)
parsing.py - для парсингу даних з сайтів
main.py - основний файл для запуску бота

## bot_logic 
1. витягнути час оновлення з сайту
2. перевіти чи є нові данні, чи час змінився (зберігати у json)
3. зайти на сайт і дістати данні - parsing.py
4. Відправити в телеграм канал - main.py
5. повторити через певний час (наприклад, кожні 30 хвилин)


pip install python-dotenv

```
from dotenv import load_dotenv
import os

load_dotenv()  # завантажує змінні з .env у os.environ

bot_token = os.getenv("BOT_TOKEN")
```