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
        currency_text += """{0}: <b>{1:>10}</b>\n""".format(currency_to_show, value)

    notification = {
        'header': 'Currencies Now',
        'text': currency_text
    }

    n = notify2.Notification(notification['header'], notification['text'])
    n.show()
    n.set_timeout(100)


def timezone_notification():
    utc = arrow.utcnow()

    tz_text = ""

    for tz in SETTINGS['timezones']['to_show']:
        tz_date = utc.to(tz).format("HH:mm")
        city = tz.split("/")
        print(city, len(city))
        size = len(tz_text)
        tz_text += """{0:<12}<b>{1:>12}</b>\n""".format(city[1], tz_date)

    notification = {
        'header': 'Timezones',
        'text': tz_text
    }

    n = notify2.Notification(notification['header'], notification['text'])
    n.show()
    n.set_timeout(100)

if __name__ == '__main__':
    currency_notification()
    timezone_notification()