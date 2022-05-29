ficha = []
while True:
    print("1 - cadastro")
    print("2 - ficha")
    print("3 - Sair")
    resposta = int(input("oque voce gostaria de ver:"))
    if resposta == 2:
            print("NOME    IDADE   TELEFONE")
            for c in ficha:
                print(c[0])
                print(c[1])
    if resposta == 1:
        nome = str(input("digite o seu nome:"))
        idade = int(input("digite a sua idade:"))
        telefone = int(input("digite o seu telefone"))
        ficha.append([nome,idade,telefone])
    if resposta == 3:
        break

     
