"""main module."""
import notify2
import requests
from utils import get_settings, APIS


notify2.init("notification_init")

SETTINGS = get_settings()

request = requests.get(APIS.get('fixer', '').format(SETTINGS['currency']['base']))
response = request.json()


currency_text = str()

for currency_to_show in SETTINGS['currency']['to_show']:
	currency_text += """{0}: {1}\n""".format(currency_to_show, response['rates'][currency_to_show])

notification = {
    'header': 'Dollar Now',
    'text': currency_text
}

n = notify2.Notification(notification['header'], notification['text'])
n.show()
n.set_timeout(100)
