import re

string = "joao, joaaao, joaoooooo, maria"

#print(re.findall(r'joa{1,}o{1,}',string))
#print(re.sub(r'joao', 'erick', string))
#print(re.findall('joao|maria', string))
#print(re.search(r'joao',string))


print(re.findall(r'[a-zA-Z]oa{1,}o{1,}',string))