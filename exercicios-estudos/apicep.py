import requests
cep = int(input("informe o seu cep:"))

api = requests.get(f"https://cep.awesomeapi.com.br/json/{cep}")
endereço = api.json()

print(endereço)