def Área(largura,comprimento):
    area = largura * comprimento
    print("a area de um terreno {} x {} é de {}m²".format(largura,comprimento,area))

largura = float(input("digite a largura:"))
comprimento = float(input("digite o comprimento:"))
Área(largura,comprimento)
