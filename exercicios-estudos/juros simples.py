juros = 0
valor = float(input("digite o valor:"))
taxa = float(input("digite a taxa:"))
tempo = int(input("digite o periodo de tempo:"))
dia = tempo * 30.41
taxaDia = 0
valorTot= 0


juros = valor * taxa * tempo

valorTot = valor + juros

taxaDia = juros/dia


print("voce deve um juros de {}".format(juros))
print("a taxa de juros por dia é de {}".format(taxaDia))
print("o valor total da divida é de {}".format(valorTot))

