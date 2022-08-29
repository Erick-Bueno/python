from operator import le
import random
from re import A
arrFroca = [""""-------
  |       |
  o       |
          |
          |
          |""","""  -------
  |       |
  o       |
  |       |
          |
          |""","""  -------
  |       |
  o       |
 /|       |
          |
          |""",
          """  -------
  |       |
  o       |
 /|\      |
          |
          |""",
          """  -------
  |       |
  o       |
 /|\      |
 /        |
          |""",
          """  -------
  |       |
  o       |
 /|\      |
 / \      |
          |"""]
arr2 = []
print("""  -------
  |       |
          |
          |
          |
          |""")
somador = 0
palavras = ["leão", "maça"]
palavra = random.choice(palavras)
palavra = list(palavra)
print(palavra)
print("numero de letras: ", end="")
for c in range(len(palavra)):
   print("_",end=" ")
palavra2 = ''.join(palavra)
print("\n")
letra = str(input("informe a letra q vc acha q tem:"))
while True:
                        if letra not in palavra:
                            print(arrFroca[somador])
                            somador = somador + 1
                            if(arrFroca[somador]==arrFroca[5]):
                                print("voce perdeu")
                                break
                            letra = str(input("informe a letra q vc acha q tem:"))
                        else:
                            print("letra encontrada")
                            indice = palavra2.index(letra)
                            arr2.insert(indice,letra)
                            print(arr2)
                            if len(arr2) == len(palavra):
                                print("voce venceu")
                                break
                            else:
                                letra = str(input("informe a letra q vc acha q tem:"))
                       
                                            

        
        
