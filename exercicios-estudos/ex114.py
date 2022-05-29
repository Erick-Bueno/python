
while True:
    print("-----------------------------------")
    print("         MENU PRINCIPAL            ")
    print("-----------------------------------")
    print("1 - Ver pessoas Cadastradas        ")
    print("2 - Cadastrar Nova pessoa          ")
    print("3 - Sair                           ")
    try:
        option = int(input("Escolha a opção:"))
        if option == 1:
            print("  -----------------------------------------------")
            print("  \n         PESSOAS CADASTRADAS  \n  ")
            print("  -----------------------------------------------")
            abrindo_arq = open('ficha.txt','r')
            for linha in abrindo_arq:
                linha = linha.rstrip()
                print(linha)
            abrindo_arq.close()
        if option > 3:
            print("ERRO DIGITE UMA OPÇÃO VALIDA")
        if option == 2:
            nome = input("digite o seu nome:")
            idade = int(input("digite a sua idade:"))
            escrevendo_arq = open('ficha.txt','a')
            escrevendo_arq.write(f'{nome:<20}{idade}' + " anos" + "\n")
            escrevendo_arq.close()

        if option == 3:
            break
    except ValueError:
        print("ERRO DIGITE UMA OPÇÃO VALIDA")
    except TypeError:
        print("ERRO DIGITE UMA OPÇÃO VALIDA")

    
      
          

