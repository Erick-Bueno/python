from datetime import datetime, timedelta
from datetime import date

import mysql.connector
data_atual = date.today()
sql = "select dataa from compra"
con = mysql.connector.connect(host = "localhost", user = "root", password = "sirlei231", database = "testando")
cursor = con.cursor()
cursor.execute(sql)
dados = cursor.fetchall()
con.close()
cursor.close()
for c in range(len(dados)):
    data = data_atual>dados[c][0]
    if data == True:
        print("atrasado")
    else:
        print("não atrasado")

