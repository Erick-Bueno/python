lista = []
nomes = []
notas = []
pergunta = "sim"
#while True:
    #nomes.append(str(input("digite o seu nome:")))
    #notas.append(int(input("digite a sua nota 1:")))
    #notas.append(int(input("digite a sua nota 2:")))
    #nomes.append(notas)
    #pergunta = str(input("quer continuar:"))
    #if pergunta == "n" or pergunta == "não":
        #break
#print(nomes)

while True:
    while pergunta == "sim":
        nome = str(input("digite o seu nome:"))
        nota1 = int(input("digite sua nota1:"))
        nota2 = int(input("digite sua nota2:"))
        lista.append([nome,[nota1,nota2]])
        pergunta = str(input("quer continuar [s/n]:"))
        if pergunta == "n" or pergunta == "não":
                    break
    break

for c in lista:
    
    print(c[0])
