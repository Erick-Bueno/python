def notas(*n,sit = False):
    """
    NOTAS = PODE INFORMAR VARIAS NOTAS.
    """
    me = 0
    media = 0
    dic = {}
    maior = 0
    menor = 0
    if sit == False:
        for c in range(len(n)):
            if c == 1:
                maior = n[c]
                menor = n[c]
            else:
                if n[c] > maior:
                    maior = n[c]
                if n[c] < menor:
                    menor = n[c]
        for m in range(len(n)):
            me = me + n[m]
            media = me/len(n)
        
        dic['total'] = len(n)
        dic['maior'] = maior
        dic['menor'] = menor
        dic['media'] = media
        print(dic)
    if sit == True:
        for c in range(len(n)):
            if c == 1:
                maior = n[c]
                menor = n[c]
            else:
                if n[c] > maior:
                    maior = n[c]
                if n[c] < menor:
                    menor = n[c]
        for m in range(len(n)):
            me = me + n[m]
            media = me/len(n)
        dic['total'] = len(n)
        dic['maior'] = maior
        dic['menor'] = menor
        dic['media'] = media
        if media >= 7:
            dic['situação'] = "boa"
        if media < 7 and media > 5:
            dic['situação'] = "razoavel"
        if media <= 5:
            dic['situação'] = "ruim"
        
        help(notas)
        print(dic)
    
        
        















notas(2,8,3,6,1,10,sit = True)

