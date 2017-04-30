import json


APIS = {
    'promasters': 'http://api.promasters.net.br/cotacao/v1/valores?moedas={}',
    'fixer': 'http://api.fixer.io/latest?base={}'
}


def get_settings():
    with open('settings.json', 'r') as json_file:
        return json.load(json_file)
