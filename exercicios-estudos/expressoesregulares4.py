import re
texto = ''' <p>ola</p> <div>safe</div>'''

print(re.findall(r'<[pdiv]{1,}>(.*?)<\/[pdiv]{1,}>', texto))

#{1,} PODE TER DE 1 A INFINITAS LETRAS
#. RETORNA QUALQUER CARACTER
# * RETORNA QUALQUER VALOR DE 0 AO INFINITO/ DETERMINA A QUANTIDADE DE VEZES Q AS LETRAS APARECEM
