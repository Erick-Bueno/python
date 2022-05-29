pares = []
pergunta2= "sim" 
while True:
    while pergunta2 == "sim" or pergunta2 == "s":
        pergunta = int(input("digite um numero:"))
        pergunta2 = str(input("quer continuar [S/N]"))
        pares.append(pergunta)
        if pergunta2 == "não" or pergunta2 == "n":
            print(pares)

