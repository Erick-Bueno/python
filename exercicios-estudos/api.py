import requests
import json

def buscar_filme(filme):
    try:
            req = requests.get(f"https://www.omdbapi.com/?apikey=30dc38b3&t='{filme}'?")
            dicicionario = req.json()
            print("Titulo:",dicicionario['Title'])
            print("Ano:", dicicionario["Year"])
            print("Atores:", dicicionario["Actors"])
            print("Nota:", dicicionario["imdbRating"])
    except:
            print("filme não encontrado")

while True:
    filme = str(input("informe o filme:"))
    buscar_filme(filme)
    continuar = str(input("quer continuar?:")).upper()
    while True:
        if continuar not in "SN":
            print("digite apenas S ou N")
            continuar = str(input("quer continuar?:")).upper()
        else:
            if continuar == "S" or continuar == "SIM":
                filme = str(input("informe o filme:"))
                buscar_filme(filme)
                continuar = str(input("quer continuar?:")).upper()
            if continuar == "N" or continuar == "NÃO" or continuar == "NAO":
                break
    break
            
    
