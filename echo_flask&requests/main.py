from flask import Flask, request
import requests
import my_data

URL = f"https://api.telegram.org/bot{my_data.api_token}/"
app = Flask(__name__)


def send_text(data):
    requests.post(URL + 'sendMessage', json=data)


def parse_text(data):
    data = {
        'chat_id': data['message']['chat']['id'],
        'text': data['message']['text'],
        'reply_to_message_id': data['message']['message_id']
    }
    return data


@app.route('/', methods=['POST'])
def main():
    if request.method == 'POST':
        resp = request.get_json()
        if 'text' in resp['message']:
            send_text(parse_text(resp))
    return '...'


if __name__ == '__main__':
    app.run()
