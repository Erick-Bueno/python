import random
from time import sleep
posiçao = 0
pontos = 1
jogo = {}
jogo[1] = random.randint(1,6)
jogo[2] = random.randint(1,6)
jogo[3] = random.randint(1,6)
jogo[4] = random.randint(1,6)
print("o jogador 1 tirou {}".format(jogo[1]))
sleep(0.5)
print("o jogador 2 tirou {}".format(jogo[2]))
sleep(0.5)
print("o jogador 3 tirou {}".format(jogo[3]))
sleep(0.5)
print("o jogador 4 tirou {}".format(jogo[4]))
for c in range(0,4):
    posiçao = posiçao + 1
    sleep(0.5)
    print(" o {}º lugar ficou com = {}".format(posiçao, jogo[pontos]))
    pontos = pontos + 1
