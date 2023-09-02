import os
import shutil

import requests


def get_categories():
    response = requests.get('http://127.0.0.1:8000/api/category/')
    return response.json()['results']


def get_cat_id(name):
    res = dict()
    for c in get_categories():
        res[c['name']] = c['id']
    print(res)
    return res[name]


def get_products(cat, page=1, per_page=6):
    response = requests.get(
        f'http://127.0.0.1:8000/api/product/?category={cat}&page={page}&per_page={per_page}'
    )
    response_data = response.json()
    for data in response_data:
        img_url = data.get('image')
        if img_url:
            file_format = img_url.split('.')[-1]
            path = f"downloads/images/"
            file_name = f"img.{data['id']}.{file_format}"
            r = requests.get(img_url, stream=True)
            if r.status_code == 200 and not (file_name in os.listdir('downloads/images')):
                print(file_name, 'downloading...')
                with open(path + file_name, 'wb') as f:
                    r.raw.decode_content = True
                    shutil.copyfileobj(r.raw, f)
    return response_data


def bot_login(phone_number, password):
    response = requests.post(
        f'http://127.0.0.1:8000/api/login/',
        data={
            'phone_number': phone_number,
            'password': password
        })
    return response.status_code, response.json()


# get_products(1)
# bot_login('1111','1111')

def get_my_cart():
    response = requests.get(
        f'http://127.0.0.1:8000/api/cart/',
        headers={
            'Authorization': f'Token e12450d93ff185d556816877498597c1c3e70c33ba123ee4903f14a5821c00f0'
        })
    print(response.json())


get_my_cart()
