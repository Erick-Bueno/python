termo = int(input("quantos termos voce quer:"))
c = termo
c1=0
c2=1
c3=1
print("0","1","1",end = " ")
while c > 0:
    c = c - 1
    c1 = c2
    c2 = c3
    c3 = c1 + c2
    print(c3, end = " ")
