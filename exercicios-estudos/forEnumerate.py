ficha = []

while True:
    nome = str(input("digite o seu nome:"))
    nota1 = float(input("digite a sua nota 1:"))
    nota2 = float(input("digite a sua nota 2:"))
    pergunta = str(input("deseja continuar:"))
    media = (nota1 + nota2)/2
    ficha.append([nome,[nota1,nota2],media])
    if pergunta == "n" or pergunta == "não":
        break
for i, c in enumerate(ficha):
    print(c[0])


    

 
