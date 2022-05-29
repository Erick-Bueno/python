lista = [1903.98, 922.66, 924.39, 913.62]
lista2= [0.075, 0.15, 0.225, 0.275]
nova_renda = 0
nova_renda2 = 0
renda = float(input("qual a sua renda:"))
salario = renda
if renda < lista[0]:
        print("IR a pagar é de 0")
for c in range(len(lista)):
    if renda > lista[c]:
        nova_renda = renda - lista[c]
        renda = nova_renda
        print(renda)
            
            
            
            
        
        
    
    
        

