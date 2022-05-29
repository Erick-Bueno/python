import random
numeros = []
def sorteia():
    print("sorteando 5 valores da lista:",end= " ")
    for c in  range(0,5):
        numeros.append(random.randint(0, 10))#numeros diferentes usa-se random.sample
    for i in numeros:
       print(i,end=" ")
sorteia()

def somapar():
    soma2 = 0
    print("\nA soma dos valores pares:",numeros,"é igual a:",end= " ")
    for c in range(len(numeros)):
        if numeros[c]%2 == 0:
            soma2 = soma2 + numeros[c]
    print(soma2)
            
        
    

somapar()






