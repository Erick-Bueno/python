dados = {}
dados['nome'] = str(input("nome:"))
data = int(input("data de nascimento:"))
idade = 2021 - data
dados['idade'] = idade
dados['carteira de trabalho'] = int(input("carteira de trabalho (0 não tem):"))
if dados['carteira de trabalho'] > 0:
    dados['ano de contratação'] = int(input("ano de contratação:"))
    dados['salario'] = float(input("salario:"))
    aposen = (dados['ano de contratação'] + 35) - 2021
    aposen2 = dados['idade']+ aposen
    dados['aposentadoria'] = aposen2
for k, v in dados.items():
    print("O(a) {} é igual a {}".format(k, v))
