def voto(idade):
   idade = 2021 - n
   if idade < 18:
       print("com", idade ,"anos voto negado")
   if idade >= 18 and idade < 65:
       print("com", idade ,"anos voto obrigatorio")
   if idade > 65:
       print("com", idade ,"anos voto opcional")
    







n = int(input("em que ano voce nasceu:"))
voto(n)


