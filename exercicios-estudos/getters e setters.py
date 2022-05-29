class valor:
    def __init__(self, num):
        self.num = num
        
    def mostrar_valor(self):
        print(self.num)     
    @property
    def num (self):
        return self._num
    
    @num.setter
    def num (self, vallor):
        for c in range (0,5):
            vallor = vallor + c
        self._num = vallor
        
       


pergunta = int(input("informe um valor:"))
v1  = valor(pergunta)
v1.mostrar_valor()





        
