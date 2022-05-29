nome = 0
peso = 0
lista = []
total = 0
pergunta = "sim"
while True:
    while pergunta == "sim":
        nome = str(input("digite o seu nome:"))
        peso = int(input("digite o seu peso:"))
        lista.append(nome)
        total = total + 1
        lista.append(peso)
        pergunta = str(input("quer continuar[S/N]:")
        if pergunta == "não" or pergunta == "n":
            print("foram cadastradas () pessoas".format(total))
