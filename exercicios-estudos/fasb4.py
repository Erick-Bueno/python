idade = int(input("qual a sua idade?:"))
sexo = str(input("informe seu sexo[M/F]:"))
if idade < 18:
    anos_faltam = 65 - idade
    print("você é jovem, ainda faltam {} anos para sua aposentadoria".format(anos_faltam))
elif idade >= 18 and idade < 60:
    anos_faltam2 = 65 - idade
    print("voce é adulto, ainda faltam {} anos para sua aposentadoria".format(anos_faltam2))
elif idade >= 65 and sexo == "M" or sexo == "Masculino":
    print("você é idoso, e já pode receber aposentadoria")
elif idade >= 60 and sexo == "F" or sexo == "Feminino":
    print("você é idosa, e já pode receber aposentadoria")
