from distutils.filelist import findall
import re

texto = """
Setor 1 ativo
setor 2 inativo
setor 3 ativo
setor 4 ativo
"""

print(re.findall(r'[a-zA-Z]{1,} ([0-9]{1,}) (?=ativo)',texto))
print(re.findall(r'^[a-zA-Z]{1,} [0-9]{1,} [a-zA-Z]{1,}$',texto, flags=re.M|re.S))
print(re.findall(r'(?=.{1,}[^in]ativo).{1,}', texto))