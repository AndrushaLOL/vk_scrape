import vk_api
from get_token import get_token
import json
from dotenv import load_dotenv
from tqdm import tqdm

load_dotenv()

import os


payload = {
    'grant_type': os.getenv('GRANT_TYPE'),
    'client_id': os.getenv('CLIENT_ID'),
    'client_secret': os.getenv('CLIENT_SECRET'),
    'username': os.getenv('LOGIN'),
    'password': os.getenv('PASSWORD')
}

token = get_token(payload)
app_id = os.getenv('APP_ID')
vk_session = vk_api.VkApi(app_id=app_id, token=token)
api = vk_session.get_api()

def get_all_dialogs_ids():
    d = api.messages.getConversations(count=1)
    count = d['count']
    res = []
    offset = 0
    c = 200
    while count > 0:
        if count > 200:
            c = 200
        else:
            c = count
        d = api.messages.getConversations(offset=offset, count=c)
        for conv in d['items']:
            conv = conv['conversation']
            if conv['peer']['type'] != 'user' or conv['peer']['id'] == 100:
                continue
            res.append(conv['peer']['id'])
        offset += c
        count -= c
    return res


def get_all_messages(idx):
    m = api.messages.getHistory(user_id=idx, count=1)
    count = m['count']
    old_c = m['count']
    offset = 0
    messages = []
    s = 0
    with tqdm(total=count) as pbar:
        while count > 0:
            new_ms = api.messages.getHistory(user_id=idx, offset=offset, count=200, rev=1)
            messages.extend(new_ms['items'])
            s = len(messages)
            pbar.update(len(new_ms['items']))
            offset += 200
            count -= len(new_ms['items'])
    return messages
        


def get_all_dialogs():
    print('Getting dialogs...')
    ids = get_all_dialogs_ids()
    print(f'found {len(ids)} dialogs')
    res = {}
    for i in ids:
        response = api.users.get(user_ids=i)
        user = response[0]
        username = user['first_name'] + '_' + user['last_name']
        print(f'Donwloading for {username}, link: https://vk.com/id{i}')
        res[i] = get_all_messages(i)
    return res

messages = get_all_dialogs()

with open('messages.json', 'w+') as f:
    f.write(json.dumps(messages))


