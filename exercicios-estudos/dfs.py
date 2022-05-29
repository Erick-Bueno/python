print("------- VALORES DAS FAIXAS ---------")
print("FAIXA 1 = 1,903.98")
print("FAIXA 2 = 922.66"  )
print("FAIXA 3 = 924.39"  )
print("FAIXA 4 = 913.62"  )
Base_atual = 0
novo_valor = 0
def IR():
    valorir = 0
    valorir2 = 0
    valorfaixa1 = 1903.98
    valorfaixa2 = 922.66
    valorfaixa3 = 924.39
    valorfaixa4 = 913.62
    Base = float(input("digite sua renda mensal:"))
    Base_atual = Base
    if Base < valorfaixa1:
         print("valor 0 de ir")

    if Base > valorfaixa1:
         Base = Base - valorfaixa1
         valorir = valorir + valorfaixa1 * 0
    
         if Base < valorfaixa2:
              valorir = Base * 0.075
        
         if Base > valorfaixa2:
              Base = Base - valorfaixa2
              valorir = valorir + valorfaixa2 * 0.075
              if Base < valorfaixa3:
                   valorir = valorir + Base * 0.15
            
              if Base > valorfaixa3:
                   Base = Base - valorfaixa3
                   valorir = valorir + valorfaixa3 * 0.15
                   if Base < valorfaixa4:
                        valorir = valorir + Base * 0.225
                
                   if Base > valorfaixa4:
                        Base = Base - valorfaixa4
                        valorir = valorir + valorfaixa4 * 0.225
                        if Base > 0:
                             valorir = valorir + Base * 0.275
                   
    aliquota = valorir/Base_atual
    print("o ir a pagar é de {}".format(valorir))
    print("a aliquota é de {}".format(aliquota))
    print("voce ira receber {}".format(Base_atual-valorir))
IR()
    
