lista = [5, 1, 4,10, 8, 3]
mais_alto = 0
menor = 0
for c in range(len(lista)): 
    if c == 1:
        mais_alto = lista[c]
        menor = lista[c]
    else:
        if mais_alto < lista[c]:
            mais_alto = lista[c]
        if menor > lista[c]:
            menor = lista[c]
print(menor)
        
         
