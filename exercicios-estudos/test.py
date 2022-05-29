peso = 0
listanome_peso = []
lista = []
total = 0
maior = 0
menor = 0
nome = 0
nome2 = 0
while True:
    listanome_peso.append(str(input("digite o seu nome:")))
    listanome_peso.append(float(input("digite o seu peso:")))
    if len(lista) == 0:
        maior = listanome_peso[1]
        menor = listanome_peso[1]
    else:
        if listanome_peso[1] > maior:
            maior = listanome_peso
        if listanome_peso[1] < menor:
            menor = listanome_peso
    pergunta = str(input("quer continuar:"))
    lista.append(listanome_peso[:])
    listanome_peso.clear()
    total = total + 1
    if pergunta in 'Nn':
        break
print("foram cadastradas {} pessoas".format(total))
print("o maior peso foi de {}".format(maior))
print("o menor peso foi de {}".format(menor))
         

   
    

        
        
    
        
       



   
           
