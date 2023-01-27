import time

import vk_api
import random


def post_wall_vk(login, password, list_publics, messages):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()

    upload = vk_api.VkUpload(vk_session)

    for i in list_publics:
        print(f"Отправляю в {i.strip()}")
        vk_session.method("wall.post", {
            'owner_id': i,
            'message': messages,
            'attachment': '',
        })
        time.sleep(random.randint(10, 20))

with open('messages.txt', 'r', encoding='utf8', errors='ignore') as txt_file:
    messages =  random.choice(txt_file.readlines())


with open('groups.txt', 'r', encoding='utf8', errors='ignore') as txt2_file:
    list_publics = txt2_file.readlines()

with open('config.txt', 'r', encoding='utf8', errors='ignore') as txt_file:
    auth = txt_file.readlines()
try:

    post_wall_vk(login=auth[0].strip(), password=auth[1].strip(), list_publics=list_publics, messages=messages)
except Exception as err:
    print('Ошибка', err)
    input()
