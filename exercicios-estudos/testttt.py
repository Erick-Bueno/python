dic = {}
gols = []
soma = 0
pergunta = 0
for c in range(0,4):
    gols.append(int(input('quantos gols voce fez:')))
    dic['gols'] = gols
for n in gols:
    soma = soma + n
    print(soma)
    
