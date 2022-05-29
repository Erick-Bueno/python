def calculadoraAdicaoSubtracao(numero, outroNumero, operacao):
    if operacao == '+':
        resultado = numero + outroNumero
        print("a soma de",numero, "+", outroNumero,"é igual a:", resultado)
    if operacao == '-':
        resultado = numero - outroNumero
        print("a subtração de",numero, "-", outroNumero,"é igual a:", resultado)
    else:
        print("o resultado é 0")

calculadoraAdicaoSubtracao(2,1,"=")

