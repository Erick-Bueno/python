animais = []
while True:
    try:
        numero = int(input('quantos animais voce quer adicionar:'))

        for c in range(0,numero):
            animal = str(input("quer adicionar qual animal na lista:"))
            if animal not in animais and not animal.isnumeric() :
                animais.append(animal)
        break
    except:
        print("digite um valor valido")
print(animais)
