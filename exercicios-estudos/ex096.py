dic  = {}
duvida = "sim"
gols = []
geral = []
soma = 0

while True:
    while duvida == "sim":
        dic['nome'] = str(input("digite o seu nome:"))
        dic['partidas'] = int(input("quantas partidas jogou:"))
        for c in range(0,dic['partidas']):
            gols.append(int(input("quantos gols na partida {}:".format(c))))
            dic['gols'] = gols[:]
        gols.clear()
        geral.append(dic.copy())
        duvida = str(input("quer continuar [S/N]:"))
        if duvida == "nao" or duvida == "n" or duvida == "N" or duvida == "Não" or duvida == "não":
            print(geral)
            break
    break
print("cod nome      gols      total")
for c in range(len(geral)):
    print(c,geral[c]['nome'],geral[c]['gols'],sum(geral[c]['gols']))
while True:
    dados = int(input("mostrar dados de qual jogador[999 pra parar]:"))
    if dados == 999:
        print("finalizado")
        break
    if dados > len(geral)-1:
        print("jogador n encontrado")
    else:
        print("levantamento do jogador",geral[dados]["nome"])
        for i, g in enumerate(geral[dados]['gols']):
            print("no jogo {} fez {}".format(i, g))
        
            
   
