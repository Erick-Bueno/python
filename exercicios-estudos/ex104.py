def ficha(n,g):
    if n == "":
        n = "desconhecido"
    if g == "":
        g = "0"
    if g in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        g = "0"
    print("o jogador",n,"marcou",g,"gols no campeonato")










n = str(input("informe o seu nome:"))
g = str(input("informe o numero de gols:"))

ficha(n,g)
