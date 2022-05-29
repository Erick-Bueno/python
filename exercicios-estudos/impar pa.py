import random
tentativas = 0

while True:
    computador = random.randint(1, 10)
    print(computador)
    player = int(input("digite o valor que voce quer de 1 a 10:"))
    escolha = str(input("voce escolhe par ou impar:")).upper()
    if (computador + player)% 2 == 0 and escolha == "PAR" or escolha == "P" or (computador + player)% 2 == 1 and escolha == "impar" :
        tentativas = tentativas + 1
        print("player ganhou")
    if (computador + player)% 2 == 0 and escolha == "IMPAR" or escolha == "I" or escolha == "ÍMPAR" or (computador + player)% 2 == 1 and escolha == "par":
        break
print("computador ganhou")
print("voce teve {} vitorias em sequencia".format(tentativas))

         

 
