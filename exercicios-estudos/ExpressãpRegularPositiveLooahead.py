import re
senha = "#123E1er"
maiscu = (re.findall(r'(?=.*[A-Z])(?=.*[a-z])(?=.*[0-9])(?=.*[\u0020-\u002f-\u003A-\u0040\-\u005B-\u0060-\u007B-\u007E]).{8}',senha))
if maiscu == []:
    print("senha invalida, verifique se a sua senha atende aos requisitos: ter 8 caracteres, conter numero, letra maiscula e caracter especial")
else:
    print("valida")

    #(?=.*[A-Z]) vai pegar qualquer coisa mais as letras mausculas, (?=[A-Z]) vai verificar se tem letras de AZ maiscula na string




