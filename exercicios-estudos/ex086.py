principal = []
linha1 = []
linha2 = []
linha3 = []
totpar = 0
totpar2 = 0
totpar3 = 0
par = 0
valor = 0
maior = 0
for c in range(1,4):
    valor = int(input("digite um valor para a matriz:"))
    linha1.append(valor)
    if valor % 2 == 0:
        totpar = totpar + valor
principal.append(linha1[:])

for c in range(1,4):
    valor = int(input("digite um valor para a matriz:"))
    linha2.append(valor)
    if valor % 2 == 0:
        totpar = totpar + valor
    valor > maior
    maior = valor
principal.append(linha2[:])

for c in range(1,4):
    valor = int(input("digite um valor para a matriz:"))
    linha3.append(valor)
    if valor % 2 == 0:
        totpar = totpar + valor
principal.append(linha3[:])
soma = principal[0][2] + principal[1][2] + principal [2][2]
print("a soma dos valores da terceira coluna é de",soma)
print("soma de todos os pares = {}".format(totpar))
print("o maior valor da segunda linha é {}".format(maior))
print("==================================")
print("[{:^5}]".format(principal[0][0]),end = " ")
print("[{:^5}]".format(principal[0][1]),end = " ")
print("[{:^5}]".format(principal[0][2]))
print("[{:^5}]".format(principal[1][0]),end = " ")
print("[{:^5}]".format(principal[1][1]),end = " ")
print("[{:^5}]".format(principal[1][2]))
print("[{:^5}]".format(principal[2][0]),end = " ")
print("[{:^5}]".format(principal[2][1]),end = " ")
print("[{:^5}]".format(principal[2][2]))
