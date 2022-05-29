ficha = []
pergunta = "sim"
while True:
   while pergunta == "sim":
      nome = str(input("digite o seu nome:"))
      nota1 = float(input("digite nota1:"))
      nota2 = float(input("digite nota2:"))
      media = (nota1 + nota2)/2
      ficha.append([nome,[nota1,nota2],media])
      pergunta = str(input("quer continuar:"))
      if pergunta == "n" or pergunta == "não":
          break
   break
print("BOLETIM")
for i,  c in enumerate (ficha): #mesma coisa que for c in lista, oq muda e q usando o enumerate voce consegue imprimir os valores do indice
    print(i,c[0],"sua media foi de",c[2])
while True:
    perguntaaa = int(input("digite o indicie do aluno que voce gostaria de ver a nota, 999 é para sair:"))
    if perguntaaa == 999:
        break

#ESSE IF E uma verificação onde cada elemento da lista e subtraido por 1 e entt verificasse se o valor digitado em perguntaaa e menor ou igual a algum elemento na lista
    if perguntaaa <= len(ficha)-1:
       #se o numero digitado e o mesmo ou menor q o de algum elemento da lista entt é imprimido os valores ,
       #exemplo digitei 2 nomes na lista, na pergunta eu digito que quero saber as notas do elemento contido no indice 1, entt o progama entra no laço de repetição e faz a vereficação
       #como eu digite 2 elementos entt no len(ficha)-1 acontece isso: 1-1 =0, 2-1=1, entt verificasse na lista se tem algum elemento igual ou menor ao que eu digite
       #nesse caso tem eu digitei 1 e na lista contem os valores 0 e 1 entt ele vai pro print,
       #onde ele imprimi a lista: ficha, nas posições [1]:,lembrando q esse 1 foi oq eu digitei, que é o indice do segundo nome , e [0] que e a lista de nomes.
       #e imprimi tbm as notas nesse caso como eu digitei 1 ele imprimi as notas do aluno no indice 1 ou seja [1],e o segundo [1] e o indice da lista de notas;
       print("notas do aluno {} são {}".format(ficha[perguntaaa][0],ficha[perguntaaa][1]))
 
   
