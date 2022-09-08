import re
cpf = "er1ick"
cpf_validator = re.findall(r'^[a-zA-Z]{1,}$', cpf)
print(cpf_validator)