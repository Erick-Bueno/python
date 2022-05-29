tupla = ("cu", "pau", "leite")
for c in tupla:
    print("\n ",c, "............", end=" ")
    for l in c:
       if l in "aeiou":
           print(l, end = " ") 