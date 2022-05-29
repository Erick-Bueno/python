maior = 0
lista = [100, 500 , 700]
listan = []
lista2 = []
for c in range(len(lista)):
    if c == 1:
        maior = lista[c]
    else:
        if lista[c] > maior:
            maior = lista[c]
print(maior)


for n in range(0,maior+1):
    if n in lista:
        listan.append(n)
print(listan)


for n in range(maior+1, 0,-1):
    if n in lista:
        lista2.append(n)
print(lista2)

        
    
    
