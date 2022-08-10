import requests
import json

moeda = str(input("informe a moeda:")).upper()

requisicao = requests.get(f"https://economia.awesomeapi.com.br/last/{moeda}")
dados = requisicao.json()
print(dados[moeda + "BRL"]["high"])