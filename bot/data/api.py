import requests
# from data.config import BASE_URL
import json

BASE_URL = 'http://127.0.0.1:8000/'

def create_user(telegram_id, username, full_name, is_active):
    url = BASE_URL + 'botuser/'
    data = {
        'tg_id': telegram_id,
        'username': username,
        'full_name': full_name,
        'is_active': is_active
    }
    response = requests.post(url, data=data)
    return response.status_code

def update_phone(telegram_id, phone):
    url = BASE_URL + f'botuser/{telegram_id}/'
    data = {
        'phone_number': phone
    }
    response = requests.patch(url, data=data)
    return response.status_code
    # print(response.json())

def update_full_name(telegram_id, full_name):
    url = BASE_URL + f'botuser/{telegram_id}/'
    data = {
        'full_name': full_name
    }
    response = requests.patch(url, data=data)
    return response.status_code
def update_user_full_name(telegram_id, full_name):
    url = BASE_URL + f'botuser/{telegram_id}/'
    data = {
        'user_full_name': full_name
    }
    response = requests.patch(url, data=data)
    return response.status_code
def update_tg_username(telegram_id, username):
    url = BASE_URL + f'botuser/{telegram_id}/'
    data = {
        'username': username
    }
    response = requests.patch(url, data=data)
    return response.status_code
def get_all_users():
    url = BASE_URL + 'botuser/'
    response = requests.get(url)
    return response.json()

def get_user_by_id(tg_id):
    url = BASE_URL + f'botuser/{tg_id}/'
    response = requests.get(url)
    return response.json()

def get_sources():
    url = BASE_URL + 'document/'
    response = requests.get(url)
    return response.json()

def get_sources_by_id(title):
    url = BASE_URL + f'document/{title}/'
    response = requests.get(url)
    return response.json()

def get_groups(course):
    url = BASE_URL + f'group/?kurs={course}'
    response = requests.get(url)
    return response.json()

def get_group_schedule(group_id):
    url = BASE_URL + f'schedule/{group_id}/group/'
    response = requests.get(url)
    return response.json()

def get_user_with_name(full_name):
    url = BASE_URL + f'getuser/{full_name}/'
    response = requests.get(url)
    return response.json()

### get user with name success
# a = get_user_with_name(full_name='𝕵𝖆𝖑𝖔𝖑𝖎𝖉𝖉𝖎𝖓 ️')
# print(a)

### create user success
# a = create_user(telegram_id=22123, username='username', full_name='jaloliddin', is_active=True)
# print(a)
    

### update phone success
# b = update_phone(telegram_id=973108256, phone='932977419')
# print(b)

### update full_name success
# c = update_full_name(telegram_id=223, full_name='full_name')
# print(c)

### get all users success
# a = get_all_users()
# print(a)

### get user by id success
# a = get_user_by_id(tg_id=973108256)
# print(a)

### get sources success
# a = get_sources()
# print(a)

### get sources by id success
# a = get_sources_by_id(title='Signallar amaliy')
# print(a)

### get groups success
# a = get_groups()
# print(a)

### get group schedule success
# a = get_group_schedule(1)
# print(a)