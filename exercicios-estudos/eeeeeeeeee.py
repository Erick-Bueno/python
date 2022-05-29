
     print("------- VALORES DAS FAIXAS ---------")
     print("FAIXA 1 = 1,903.98")
     print("FAIXA 2 = 922.66"  )
     print("FAIXA 3 = 924.39"  )
     print("FAIXA 4 = 913.62"  )
     Base_atual = 0
     novo_valor = 0
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
     salario_recebido = Base_atual-valorir
     print("o ir a pagar é de {}".format(valorir))
     print("a aliquota é de {}".format(aliquota))
     print("voce ira receber {}".format(salario_recebido))

     print("""faixa INSS
      Faixa1 = 82,50
      faixa2 = 99,31
      Faixa3 = 132,20
      faixa4 = 437,96
      Total a recolher = 751,97""")


     salario_novo = 0
     salario = float(input("digite a renda real que voce ira receber apos o imposto de rendas:"))
     if salario == 1100:
         salario_novo = (salario - 1100) * 0.075
         salario_novo = salario_novo + 82.50
         print("sera aplicado um desconto de {} na sua renda pelo inss" .format(salario_novo))
     if salario >1100.01 and salario < 2203.48:
         salario_novo = (salario - 1100.01) * 0.09
         salario_novo = salario_novo + 82.50
         print("sera aplicado um desconto de {} na sua renda pelo inss" .format(salario_novo))
     if salario > 2203.49 and salario < 3305.22:
         salario_novo = (salario - 2203.49) * 0.12
         salario_novo = salario_novo + 82.5 + 99.31
         print("sera aplicado um desconto de {} na sua renda pelo inss" .format(salario_novo))
     if salario > 3305.23 and salario <= 6433.57:
         salario_novo = (salario - 3305.23) * 0.14
         salario_novo = salario_novo + 82.5 + 99.31 + 132.20
print("sera aplicado um desconto de {} na sua renda pelo inss e seu novo salario sera de {}" .format(salario_novo, salario_recebido-salario_novo))



