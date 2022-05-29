dic = {}
infos = []
duvida = "sim"
pessoas = 0
soma = 0
media = 0
mulheres = []
acimadmedia=[]
while True:
    while duvida == "sim":
       nome = str(input("digite o seu nome:"))
       idade = int(input("digite a sua idade:"))
       soma = soma + idade
       sexo = str(input("qual o seu sexo [M/F]:"))
       if sexo == "F" or sexo == "feminino" or sexo == "f":
           mulheres.append(nome)
           
       dic['nome'] = nome
       dic['idade']= idade
       dic['sexo'] = sexo
       infos.append(dic.copy())
       pessoas = pessoas + 1
       duvida = str(input("deseja continuar[s/n]:"))
       media = soma/pessoas
       if idade > media:
           acimadmedia.append(nome)
       if duvida == "nao" or duvida == "n":
            break
    break
print("foram cadastradas {} pessoas".format(pessoas))
print("a media de idade do grupo é de {}".format(media))
print("as mulheres cadastradas foram {}".format(mulheres))
print("as pessoas com idade acima da media foram {}".format(acimadmedia))

