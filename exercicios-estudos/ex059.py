fatorial = int(input("digite o numero que voce que o fatorial:"))
c = fatorial
f = 1
print(c,"!",end = " = ")
while c > 0:
    f = f * c
    c = c - 1
    print(c,end = " X ")
print("=",f)
