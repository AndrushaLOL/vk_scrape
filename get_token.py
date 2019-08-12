import requests
import json

AUTH_URL = 'https://oauth.vk.com/token'


def get_token(payload):
    r = requests.get(AUTH_URL, params=payload)
    token = json.loads(r.content)['access_token']
    return token

if __name__ == '__main__':
    get_token()
