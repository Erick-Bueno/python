import re
especiais = ".-"

cpf = str(input('informe o seu cpf:'))
if len(cpf) == 14 or len(cpf) == 11:
    validador = (re.findall(r'^[0-9]{3}\.?[0-9]{3}\.?[0-9]{3}\-?[0-9]{2}$',cpf))
    if validador == []:
        print("informe um cpf valido")
    else:
        print(validador)



  




