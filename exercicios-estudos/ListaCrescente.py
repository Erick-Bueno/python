lista = [50,434,0,500,8,5,1000]
maior = 0
listacres = []
for c in range (0, len(lista)):
    if c == lista[0]:
        maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
print(len(lista))

for c in range(0, maior +1): #vai pegando os valores para comparar
    for i in range(0, len(lista)): #faz compraçaão com todos os valores da lista
        if c == lista[i]:
            listacres.append(lista[i])
print(listacres)
            
        
        
