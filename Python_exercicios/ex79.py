valores = []
while True:
    
    valor = int(input("Digite um numero: "))
    continuar = str(input("Quer continuar [S/N]: ")).upper().split()[0]
    if valor not in valores:
        valores.append(valor)
        print("Valor adicionado.........")
    else:
        print("Valor nao adicionado, numero duplicado")
        
    if continuar in 'N':
        break
valores.sort()
print(valores)