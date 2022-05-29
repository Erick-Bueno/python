from sqlite3 import Cursor
import mysql.connector

        
def conexaoDb(sql):
   con =  mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
   cursor = con.cursor()
   cursor.execute(sql)
   con.commit()
   cursor.close()
   con.close()

     
def conexaodb2(seleciona):
   con =  mysql.connector.connect(host="localhost", password ="123456",database="banco", user = "root")
   cursor = con.cursor()
   cursor.execute(seleciona)
   dado = cursor.fetchall()
   cursor.close()
   con.close()
   
   

   





    

        







    




