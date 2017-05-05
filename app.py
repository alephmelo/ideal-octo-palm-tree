"""main module."""
import notify2
import requests
import arrow
from utils import get_settings, APIS


SETTINGS = get_settings()
notify2.init("self_explained")


def currency_notification():
    request = requests.get(APIS.get('fixer', '').format(SETTINGS['currency']['base']))
    response = request.json()
    currency_text = str()

    for currency_to_show in SETTINGS['currency']['to_show']:
        value = response['rates'][currency_to_show]
        currency_text += """{0}: <b>{1}</b>\n""".format(currency_to_show, value)

    notification = {
        'header': 'Currencies Now',
        'text': currency_text
    }

    n = notify2.Notification(notification['header'], notification['text'])
    n.show()
    n.set_timeout(100)


def timezone_notification():
    utc = arrow.utcnow()

    n = notify2.Notification("notification['header']", "notification['text']")
    n.show()
    n.set_timeout(100)

if __name__ == '__main__':
    currency_notification()
    timezone_notification()