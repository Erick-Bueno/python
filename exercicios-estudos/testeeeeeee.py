from distutils.filelist import findall
import re

cpf = "096.692.795-85"
especiais = ".-"
for c in especiais:
    cpf =  cpf.replace(c,'')
    validar = (re.findall(r'[0-9]{3}.?[0-9]{3}.?[0-9]{3}-?[0-9]{2}', cpf))
    for i in validar:
        cpf = i
print(cpf)
