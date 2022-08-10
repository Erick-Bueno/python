import requests

api = requests.get("https://economia.awesomeapi.com.br/last/USD-BRL,EUR-BRL,BTC-BRL")
moedas = api.json()

print(moedas['USDBRL']['name'])
print(moedas['USDBRL']['high'])

