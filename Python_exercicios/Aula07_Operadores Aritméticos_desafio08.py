valor = float(input("Digite  ovalor da carteira: R$:"))
dolar = 5.01
conversao = valor / dolar

print("O valor da carteira e R${}, valor do dolar ${}, total convetido em dolares e ${:.2f} ".format(valor, dolar, conversao))