def pyhelp():
    while True:
        tamanho = 43
        tamanhoo = 43
        tamanhooo = 0
        tamanhooou = 0
        texto = "SISTEMA DE AJUDA PYHELP"
        while tamanhooo < len(texto)+3:
            print("~",end="")
            tamanhooo = tamanhooo + 1
        print("\n",texto)
        while tamanhooou < len(texto)+3:
            print("~",end="")
            tamanhooou = tamanhooou + 1
        funcao = str(input("\n digite a funcao ou biblioteca:"))
        if funcao == "fim":
            print("ATE LOGO")
            break
        while tamanhoo >= len(funcao):
            print("~",end="" )
            tamanhoo = tamanhoo - 1
        print(" ", "   \n  ACESSANDO MANUAL DO COMANDO ","'",funcao,"'")
        while tamanho >= len(funcao):
            print("~",end="" )
            tamanho = tamanho - 1
        help(funcao)
        
        













pyhelp()
