def metade(n,form = False):
    metade = n/2
    if form == False:
        return metade
    if form == True:
        return moeda(metade)

def dobro(n,form = False):
    dobro = n* 2
    if form == False:
        return dobro
    if form == True:
        return moeda(dobro)

def aumento(n,form = False):
    aumento = n*1.10
    if form == False:
        return aumento
    if form == True:
        return moeda(aumento)

def desconto(n,form = True):
    desconto = n * 0.13
    desconto2 = n - desconto
    if form == False:
        return desconto2
    if form == True:
        return moeda(desconto2)

def moeda(n):
    a = "R$"
    b = n
    c = a + str(b)
    return c

def resumo(n,a,d):
    print("----------RESUMO DO VALOR----------")
    print("preço analisado:",moeda(n))
    print("dobro do preço:",moeda(n*2))
    print("metade do preço:",moeda(n/2))
    aumento = n * (a/100)
    aumento2 = aumento + n
    print(a,"% aumento:",moeda(aumento2))
    desconto = n * (d/100)
    desconto2 = n - desconto
    print(d,"% desconto:",moeda(desconto2))

def leiadinheiro(n):
    n = str(input("digite o valor:")).replace(",",".")
    while True:
        if " " in n or n.isalpha() or n.strip()== '' :
            n = str(input("digite um valor valido:"))
            
        else:
            return float(n)
        
    
            
        


         
    
    
    









