def fatorial(n,show = False):
    """
    n = numero escolhido para encontrar fatorial
    show = parametro opcional(mostrar ou não a conta)


    """
    f = 1
    if show == True:
        for c in range(n,0,-1):
            f = f * c
            if c > 0:
                print(c,"x",end=" ")
        print("=",f)
    if show == False:
        f2 = 1
        for i in range(n,0,-1):
            f2 = f2 * i
        print(f2)









numero = int(input("digite um numero:"))

fatorial(numero)
help(fatorial)
