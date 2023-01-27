import vk_api
import random

def get_random_message():
    with open('messages.txt', 'r', encoding='utf8', errors='ignore') as txt_file:
        return random.choice(txt_file.readlines())

def get_friends_public():
    with open('groups.txt', 'r', encoding='utf8', errors='ignore') as txt_file:
        return txt_file.readlines()

def post_wall_vk(login, password):
    vk_session = vk_api.VkApi(login, password)
    vk_session.auth()

    for owner_id in get_friends_public():
        vk_session.method("wall.post", {
            'owner_id': owner_id,
            'message': get_random_message(),
            'attachment': '',
        })


with open('config.txt', 'r', encoding='utf8', errors='ignore') as txt_file:
    auth = txt_file.readlines()
try:
    post_wall_vk(login=auth[0], password=auth[1])
except Exception as err:
    print('Ошибка', err)
