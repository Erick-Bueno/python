dic = {}
gols = []
soma = 0
dic['nome'] = str(input("digite o seu nome:"))
dic['partidas'] = int(input("quantas partidas jogou:"))
for c in range(0,dic['partidas']):
    gols.append(int(input("quatos gols na partida {}:".format(c))))
dic['gols'] = gols
for numeros in gols:
    soma = soma + numeros
dic['total'] = soma
print(dic)
print("==========================================================")
for k, v in dic.items():
    print("o campo {} tem o valor de {}".format(k, v))
print("==========================================================")
for c in range(len(gols)):
    print("Na partida",c,",","fez",gols[c],"gols.")



