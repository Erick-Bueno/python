montante_fin = 0
capital = int(input("informe o seu capital:"))
taxa = float(input("informe a taxa de juros:"))
periodo = int(input("informe o periodo:"))
juros = capital * taxa
montante = capital + juros
montante_fin = montante
print(montante, " essa foi a sua montante no 1 mês")
for c in range(2, periodo + 1):
    juros = montante_fin * taxa
    montante_fin = montante_fin + juros
    print("{:.2f} essa foi a sua montante no {} mês".format(montante_fin,c))
    

