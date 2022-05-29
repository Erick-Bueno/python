principal = []
par = []
impar = []
numero = 0
for c in range(1,8):
    numero = int(input("digite um numero"))
    if numero % 2 == 0:
        par.append(numero)
    if numero % 2 == 1:
        impar.append(numero)
par.sort()
impar.sort()
principal.append(impar)
principal.append(par)
print("lista principal {}".format(principal))
print("os valores impares digitados foram{}".format(principal[0]))
print("os valores pares digitados foram {}".format(principal[1]))
      
