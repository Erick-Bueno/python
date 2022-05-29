import re

string = "diario de Erick,ola meu nome é erick e essa é minha mãe sirlei, Sirlei"

#print(re.findall(r'erick|sirlei',string))
#print(re.findall(r'erick|s.....',string))
print(re.findall(r'([a-zA-Z]rick)|[a-zA-Z]irlei',string))
#print(re.findall(R'eRick|sIrlei',string, flags= re.I))
