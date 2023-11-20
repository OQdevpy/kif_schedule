import requests
import json

BASE_URL = 'https://mamatmusayev.uz/api/'


def create_user(telegram_id, username, full_name, is_active):
    url = BASE_URL + 'users/'
    data = {
        'telegram_id': telegram_id,
        'username': username,
        'full_name': full_name,
        'is_active': is_active
    }
    response = requests.post(url, data=data)
    # print(response.json())


    
    