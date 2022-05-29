situaçao = {}
situaçao['nome'] = str(input("nome:"))
situaçao['media'] = float(input("media de {}:".format(situaçao['nome'])))
print("o nome é igual a {}".format(situaçao['nome']))
print("media é igual a {}".format(situaçao['media']))
if situaçao['media'] >= 5 and situaçao['media'] < 7:
    print("situação é igual a recuperação")
if situaçao['media'] < 5:
    print("situação igual a reprovado")
if situaçao['media'] >= 7:
    print("situação igual a aprovado")
    
