"""main module."""
import notify2
import requests
from utils import get_settings, APIS


notify2.init("notification_init")

SETTINGS = get_settings()

request = requests.get(APIS.get('fixer', '').format(SETTINGS['currency']['base']))
response = request.json()

notification = {
    'header': 'Dollar Now',
    'text': """R$ {}
            """.format(response['rates']['BRL'])
}

n = notify2.Notification(notification['header'], notification['text'])
n.show()
n.set_timeout(100)
