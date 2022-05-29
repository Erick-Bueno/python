def vezesletraaparece(frase,letra):
    tot = 0
    for c in range(len(frase)):
        if letra in frase[c]:
            tot = tot+1
    print("a letra",letra,"apareceu",tot,"vezes na frase",frase)
       

vezesletraaparece("ola muundo","u")
