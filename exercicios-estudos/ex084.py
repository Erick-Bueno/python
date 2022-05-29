nome = 0
peso = 0
lista = []
princp = []
total = 0
maior = 0
menor = 0
pergunta = "sim"
while True:
    while pergunta == "sim":
        lista.append(str(input("digite o seu nome:")))
        lista.append(float(input("digite o seu peso:")))
        if len(princp)== 0:
            maior = lista[1]
            menor = lista[1]
        else:
            if lista[1] > maior:
                maior = lista[1]
            if lista[1] < menor:
                menor = lista[1]
        princp.append(lista[:])
        princp.clear()
        total = total + 1
        
        pergunta = str(input("quer continuar[S/N]:"))
        if pergunta == "não" or pergunta == "n":
            break
    break
    for p in  princp:
        if p[1] == maior:
            print(p[0])
print("foram cadastradas {} pessoas".format(total))


