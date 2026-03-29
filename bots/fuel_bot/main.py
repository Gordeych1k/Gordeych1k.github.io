from parsing import get_fuel_price
import requests
from dotenv import load_dotenv
import os
load_dotenv()  # завантажує змінні з .env у os.environ
bot_token = os.getenv("BOT_TOKEN")
chat_id = os.getenv("ID_GROUP")


def send_group(text):
    send_url = f'https://api.telegram.org/bot{bot_token}/sendMessage?chat_id={chat_id}&text={text}&disable_web_page_preview=true'
    response = requests.get(send_url)

    if response.status_code == 200:
        print("Message sent successfully")
    else:
        print("Error sending message:", response.status_code)

data = get_fuel_price()
text = f'{data[0]} {data[1]} {data[2]} {data[3]}'
send_group(text)



