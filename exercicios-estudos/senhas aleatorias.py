import random
alfabeto_minusculo = "abcdefghijklmnopqrstuvwxyz"
alfabeto_maiusculo = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
numeros = "0123456789"
caracter_especiais = "@#$&*.|/"
senha = 8
caracteres = alfabeto_maiusculo + alfabeto_maiusculo + numeros + caracter_especiais
user_password=random.sample(caracteres,senha)
print("sua senha é =",('').join(user_password))
