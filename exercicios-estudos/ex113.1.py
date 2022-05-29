def leiaint():
    while True:
        try:
            n1 = int(input("digite um valor inteiro:"))
        except ValueError:
              print("digite um numero inteiro valido")
        except KeyboardInterrupt:
            print("o usuario optou por não digitar o valor")
            return 0
            break
        else:
            return n1

def leiafloat():
    while True:
        try:
            n2 = float(input("digite um valor real:"))
        except ValueError:
              print("digite um numero real valido")
        except KeyboardInterrupt:
            print("o usuario optou por não digitar o valor")
            return 0
            break
        else:
            return n2








print("o numero inteiro foi",leiaint(),"e o numero real foi",leiafloat())


