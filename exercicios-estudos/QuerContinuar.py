continuar = str(input("quer continuar?")).upper()
while True:
    if continuar not in 'SN':
        print("digite uma resposta validade")
    continuar = str(input("quer continuar?")).upper()
    if continuar == 'N':
        break
    
