p = int(input('Qual o primeiro termo da PA? '))
r = int(input('Qual é a rasão da PA? '))
cont = 0
tot = 10
v = 1
while cont < tot:
    print(r * cont + p,end='→ ')
    cont += 1
    if cont == tot:
         v = int(input('PAUSA\nDeseja exibir mais quantos temos[?/0]? '))
         tot += v
print('Ao total foram exibidos {} termos!'.format(tot))
