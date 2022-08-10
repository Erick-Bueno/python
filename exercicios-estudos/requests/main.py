import requests

requisicao = requests.get("https://www.twitch.tv")

print(requisicao.text)