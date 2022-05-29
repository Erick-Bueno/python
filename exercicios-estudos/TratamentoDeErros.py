
       







def leiaNum():
    while True:
        try:
            i = int(input('Digite um número inteiro: '))
            break
        except ValueError:
            print("informe um valor valido para o campo inteiro")
        except KeyboardInterrupt:
            print("não foi informado nenhum valo inteiro")
            i = 0
            break
    while True:
        try:
            r = float(input('Digite um número real: '))
            break
        except ValueError:
            print("informe um valor valido para campo real")
        except KeyboardInterrupt:
            print("não foi informado nenhum valor real")
            r = 0
            break

    if i != 0 and r == 0:
        print(f"o valor real não foi encontrado e o valor inteiro informado foi o {i}")
    if i == 0 and r != 0:
        print(f"o valor inteiro não foi encontrado e o valor real informado foi o {r}")
    if i == 0 and r == 0:
        print("não foi encontrado nenhum valor nos campos")
    else:
        print(f"encontramos os valores {i} e {r} para inteiro e real respectivamente")
        
        



leiaNum()




