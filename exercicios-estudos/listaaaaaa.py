lista = []
nome = []
notas = []
while True:
    nome.append(str(input("digite o seu nome:")))
    notas.append(float(input("digite a sua nota1:")))
    notas.append(float(input("digite a sua nota2:")))
    pergunta = str(input("quer continuar:"))
    lista.append(nome)
    lista.append(notas[:])
    if pergunta == "n":
        break
print(lista)
