lista = [5, 2, 4,10, 8, 3]
mais_alto = 0
novalista = []
for c in range(len(lista)): #valor mais alto de uma lista sem usar função!
    if mais_alto < lista[c]:
        mais_alto = lista[c] 



for c in range(mais_alto+1): #repete ate o numero maximo da lista
    for i in range(len(lista)): #repete ate o numero maximo de indices da lista
        if c == lista[i]:
            print(c)
