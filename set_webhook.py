import requests
import my_data

what = input('local/server: ')
URL = f"https://api.telegram.org/bot{my_data.api_token}/"
if what == 'local':
    adress = input('way: ')
    resp = requests.post(f'{URL}setWebhook?url={adress}')
    print(resp.json())

if what == 'server':
    resp = requests.post()
    print(resp.json())

else:
    pass
