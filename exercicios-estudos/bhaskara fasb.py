import math
print("-----------------------------------")
print("       CALCULADORA BHASKARA        ")
print("-----------------------------------\n")
while True:
    try:
        a = float(input("informa o valor de a:"))
        b = float(input("informe o valor de b:"))
        c = float(input("informe o valor de c:"))
        delta = (b ** 2) - 4 * a * (c)
        if delta < 0:
    
            print("a raiz desse numero nao existe, pois o valor de delta e negativo, por favor informe novamente")
        else:
            raiz = math.sqrt(delta)
            

            x = (-b + raiz)/(2*a)
            x2 = (-b - raiz)/(2*a)
            print("as raizes da sua equação de bhaskara são {} e {}".format(x,x2))
            break

    except ValueError:
        print("digite um valor valido")
    
