import requests

try:
     if requests.head('http://pudim.com.br'):
         print("o site estaaa acessivel")
except requests.ConnectionError:
    print(" o site não esta acessivel")


        
   













