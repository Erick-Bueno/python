c = 0
soma = 0
num = int(input("digite um numero:"))
while num != 999:
    if num != 999:
        c = c + 1
        soma =soma + num
        num = int(input("continue digitando:"))
print("o a quantidade de numeros digitados foi de {} e o total é de {}".format(c, soma))

