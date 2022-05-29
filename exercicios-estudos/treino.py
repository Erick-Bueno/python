lista = []
def mask(cc):
    for c in range(len(cc)):
        if c <= len(cc)-5 :
            lista.append("#")
            
            
        else:
            lista.append(cc[c])

   
    
    for c in range(len(lista)):
        print(lista[c],end=" ")


nCartao = str(input("informe o numero do seu cartão:")).strip()
mask(nCartao)
