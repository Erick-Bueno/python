import time
media =0
soma=0
quant=0
num = 0
maior = 0
menor = 0
conti = "sim"
while conti == "sim":
     quant = quant + 1
     num = float(input("digite um numero:"))
     conti = str(input("ainda quer continuar[sim/não]:")) 
     soma = soma + num
     if quant == 1:
        maior = num
        menor = num
     else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
media =  soma /quant 
    
print("a media entre os numeros é {}, o maior valor é {} e o menor valor é {}".format(media, maior, menor))
    
