import re

string = "ola eu sou o lol"

if re.search(r"goku",string):
    print('a palavra foi encontrada')
else:
    print('a palavra não foi encontrada')

print(re.search(r'goku',string))
print(re.sub(r'goku','nappa',string))
print(re.findall(r'goku',string))


#usando o compile
lol = re.compile(r'goku')
print(lol.search(string))
print(lol.sub('vegeta',string))
print(lol.findall(string))
