import re
string = "maçaverde2"

string = (re.findall(r'^[a-záàâãéèêíïóôõöúçñÁÀÂÃÉÈÍÏÓÔÕÖÚÇÑA-Z\s]{1,}$',string))
print(string)