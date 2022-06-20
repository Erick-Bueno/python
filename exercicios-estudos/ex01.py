convidados = int(input("quantas pessoas serão convidadas:"))
lista_convidados = []
for c in range(0, convidados):
    nome = str(input("digite o nome do convidado:"))
    lista_convidados.append(nome)
print("convidados:")
for c in lista_convidados:
    print(c)

    
