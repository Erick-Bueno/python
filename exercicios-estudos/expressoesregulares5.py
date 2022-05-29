import re
texto3 = ''' <p>ola</p> <div>safe</div>'''
print(re.findall(r'<([pdiv]{1,})>.*?<\/\1>', texto3)) #oq foi salvo entre os () é retornado com o \1, porem nesse caso so é retornado os valores q estão dentro da tag

texto = ''' <p>ola</p> <div>safe</div>'''
print(re.findall(r'<(([pdiv]{1,})>.*?<\/\2)>', texto)) #para que seja retornada toda a string é necessario criar um segundo grupo envolvendo a string toda

cpf = "096.692.795-85"
print(re.findall(r'[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\-[0-9]{1,3}',cpf))

print(re.findall(r'((?:[0-9]{1,3}\.){2}[0-9]{1,3}\-[0-9]{1,3})',cpf))


data = "12/07/2003"
print(re.findall(r'((?:[0-9]{1,2}\/){2}[0-9]{1,4})',data))

rg = "12.345.678.9"
print(re.findall(r'([0-9]{1,2}\.(?:[0-9]{1,3}\.){2}[0-9]{1,2})',rg))

tags = "<h1>ola mundo</h1> <h1>lixo</h1> <p>droga</p>"
print(re.findall(r'<[h1p]{1,2}>.*?<\/[h1p]{1,2}>',tags)) #expressão normal
print(re.findall(r'<(([h1p]{1,2})>.*?<\/\2)>',tags)) #expressão com retrovisor


#?: n salva o grupo entt ele n é retornado

#primeiro verificar se ocorre alguma repetição na string
#se houver faça a expressão regular normal e coloque oq se repete em grupo, '()',e na frente o numero de vezes q se repete,{}, depois é so continuar fazendo a expressão com o resto das strings normalmente e entt envolver toda a expressão em um outro grupo, no final irão retornar 2 valores um com a string completa e outro referente ao 