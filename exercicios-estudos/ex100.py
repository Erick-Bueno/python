def numeros(*maior):
    soma = 0
    m = 0
    for i in lista:
        print(i, end = " ")
        soma = soma + 1
    for c in range(len(lista)):
        if c == 1:
            m = lista[c]
        else:
            if lista[c] > m:
                m = lista[c]

    
    print("foram informados",soma,"valores ao todo","\no maior valor informado foi o ",m)
    print("------------------------------------------------------------------------------")

lista = [1,2,3]
numeros()
lista = [100,200,5,2]
numeros()

