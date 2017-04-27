"""main module."""
import notify2
import requests


APIS = {
    'promasters': 'http://api.promasters.net.br/cotacao/v1/valores?moedas={}'
}

notify2.init("USD_Notif")

request = requests.get(APIS.get('promasters', '').format('USD'))
response = request.json()

notification = {
    'header': 'Dollar Now',
    'text': """R$ {}
            """.format(response['valores']['USD']['valor'])
}

n = notify2.Notification(notification['header'], notification['text'])
n.show()
n.set_timeout(100)
