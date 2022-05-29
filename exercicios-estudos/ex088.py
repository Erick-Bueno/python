from time import sleep
import random
numero= []
c = 0
jogos = int(input("quantos jogos voce quer que eu sorteie:"))
print(  "SORTEANDO {} JOGOS".format(jogos))    
for c in range(1,jogos + 1):
    numero = random.sample(range(0,61), 6)
    print("jogo",c,sorted(numero))
    sleep(0.5)
