from time import sleep
def contador(inicio,fim,passo):
    passo = abs(passo)
    if passo == 0:
        passo = 1
    print("\ncontagem de {} ate {} de {} em {}:".format(inicio,fim,passo,passo))
    for c in range(inicio, fim+1, passo):
            print(c,end = " ")
    if inicio > fim:
        for c in range(inicio, fim-1, -passo):
            print(c,end = " ")
        print(" ")

            
        
    
 
 
   
    


contador(1,10,1)
contador(10,0,2)
i = int(input("digite o inicio:"))
f = int(input("digite o fim:"))
p = int(input("digite o passo:"))

contador(i,f,p)

