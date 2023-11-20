import requests
from data.config import BASE_URL
import json

def create_user(telegram_id, username, full_name, is_active):
    url = BASE_URL + 'botuser/'
    data = {
        'tg_id': telegram_id,
        'username': username,
        'full_name': full_name,
        'is_active': is_active
    }
    response = requests.post(url, data=data)
    print(response.json())
    return response.status_code

def update_phone(telegram_id, phone):
    url = BASE_URL + f'botuser/{telegram_id}/'
    data = {
        'phone': phone
    }
    response = requests.patch(url, data=data)
    return response.status_code
    # print(response.json())
    
a = create_user(telegram_id=223, username='username', full_name='full_name', is_active=True)
print(a)
    
    
# b = update_phone(telegram_id=1223, phone='phone')
# print(b)