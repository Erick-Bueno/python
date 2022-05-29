ficha = {}
soma = 0
geral = []
while True:
    ficha['nome'] = str(input("digite o seu nome"))
    soma = soma + 1
    ficha['idade'] = int(input("digite a sua idade"))
    geral.append(ficha.copy())
    pergunta = str(input("quer continuar sim ou não"))
    if pergunta == "não":
        break
for c in range(0, soma):
    print(geral[c]['nome'])



  
 
    
 
