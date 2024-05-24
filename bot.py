import requests
from flask import Flask, request

app = Flask(__name__)

API_KEY = '6743547187:AAGfhT8wv-Z9Ds2NP_xItJs0Ud89o0qvyYE'
WEBHOOK_URL = 'https://api.telegram.org/bot{}/setWebhook'.format(API_KEY)

@app.route('/', methods=['POST'])
def webhook():
    update = request.get_json()
    if 'message' in update:
        handle_message(update['message'])
    elif 'callback_query' in update:
        handle_callback_query(update['callback_query'])
    return 'OK'

def handle_message(message):
    chat_id = message['chat']['id']
    text = message.get('text', '')
    user_id = message['from']['id']
    username = message['from'].get('username', '')

    if text == '/start':
        send_message(chat_id, 'مرحبا بك! يمكنك إرسال إيدي حسابك لمعرفة تاريخ تسجيله.')

def handle_callback_query(callback_query):
    # Handle callback query if needed
    pass

def send_message(chat_id, text):
    url = 'https://api.telegram.org/bot{}/sendMessage'.format(API_KEY)
    data = {'chat_id': chat_id, 'text': text}
    requests.post(url, json=data)

def get_registration_date(user_id):
    headers = {'x-api-key': 'e758fb28-79be-4d1c-af6b-066633ded128'}
    data = {'telegramId': user_id}
    response = requests.post('https://restore-access.indream.app/regdate', headers=headers, json=data)
    return response.json()['data']['date']

if __name__ == '__main__':
    requests.get(WEBHOOK_URL)
    app.run(port=5000)
