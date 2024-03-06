import requests

try:
  web_response = requests.get('https://www.pudim.com.br')
    
except:
    print('Site Insdiponivel')
else:
    print('Site disponivel')
