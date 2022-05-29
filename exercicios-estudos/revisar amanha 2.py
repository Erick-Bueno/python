tupla = ("aventura", "progamação", "tecnologia")
for c in tupla:
    print("\n","Na palavra",c,"............","temos",end=" ")
    for palavras in c:
        if palavras in "aeiou":
            print(palavras, end=" ")
