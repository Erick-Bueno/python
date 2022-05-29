lista = [100, 1000, 10, 500]
lista2 = []
lista3= []
maior = 0
for c in range(len(lista)):
    if c == 1:
        maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]

for n in range(0,maior+1):
    for n2 in range(0,len(lista)):
        if n == lista[n2]:
            lista2.append(n)
print(lista2)


            
for n in range(maior, 0,-1):
    for n2 in range(0,len(lista)):
        if n == lista[n2]:
            lista3.append(n)
print(lista3)
