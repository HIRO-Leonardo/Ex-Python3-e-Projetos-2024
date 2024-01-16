from datetime import date

ano = date.today().year
cont_maior = 0 
cont_menor = 0
for c in range(1,8):
    idade = int(input("Digite o ano que {} nasceu: ".format(c)))
    total = ano - idade
    if total >= 18:
        
        cont_maior +=1
    else:
        
        cont_menor +=1
          
print("Dos anos digitados {} sao maiores e {} sao menores".format(cont_maior, cont_menor))        
