import os

import requests
import telegram
from dotenv import load_dotenv

load_dotenv()


TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')
API_key = os.getenv('KEY')
city_name = 'Moscow'
country_code = 'ru'
units = 'metric'
lang = 'ru'
url = 'https://api.openweathermap.org/data/2.5/weather?q='

bot = telegram.Bot(token=TELEGRAM_TOKEN)

URL = (f'{url}{city_name},'
       f'{country_code}&appid={API_key}&units={units}&lang={lang}')


def get_weather():
    try:
        response = requests.get(URL)
    except requests.exceptions.RequestException as error:
        raise requests.exceptions.RequestException(error)
    try:
        return response.json()
    except ValueError as e:
        raise ValueError(e)
    except TypeError as e:
        raise TypeError(e)


def parse_weather(response):
    weather = get_weather().get('weather')
    description = weather[0]['description']
    main = get_weather().get('main')
    temp = main['temp']
    return f'На данный момент температура в Москве {temp}°С, {description}'


def send_message(message, tg_id):
    return bot.send_message(chat_id=tg_id, text=message)


def tg_bot(tg_id):
    try:
        if get_weather():
            message = parse_weather(get_weather())
            send_message(message, tg_id)
    except Exception as e:
        message = f'Ошибка при отправке погоды: {e}'
        send_message(message, tg_id)
