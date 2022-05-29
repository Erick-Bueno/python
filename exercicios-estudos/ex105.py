def leiaint(n):
    while True:
        n = str(input("digite um numero:"))
        #if n in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz":
        if n.isnumeric():
            print("voce acabou de digitar o numero",n)
            break
        else:
            print("ERRO DIGITE UM NUMERO INTEIRO VALIDO")
       
    







numero = leiaint("digite um numero:")
    
