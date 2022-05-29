gasolina = float(input("informe o valor da gasolina:"))
etanol = float(input("informe  valor do etanol:"))
CxB = etanol/gasolina
if CxB < 0.75:
    print("Etanol vale mais a pena nessa situação")
elif CxB > 0.75:
    print("Gasolina vale mais a pena nessa situação")
