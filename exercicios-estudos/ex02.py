def lista_maiorvalor(listagem):
    maior = 0
    for c in range(len(listagem)):
        if listagem[c] > maior:
            maior = listagem[c]
    print("o maior valor da lista é",maior)
def lista_menorvalor(listageem):
    menor = 0
    for i in range(len(listageem)):
        if i == 1:
            menor = listageem[i]
        else:
            if listageem[i] < menor:
                menor = listageem[i]
    print("O menor valor da lista é",menor)







lista_maiorvalor([100,2,0.5,4,5])
lista_menorvalor([100,2,0.5,4,5])
