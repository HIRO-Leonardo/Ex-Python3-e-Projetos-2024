cont = soma = num = 0 
while num != 999:
    num = int(input("Digite um numero: "))
    if num == 999:
        break
    cont += 1
    soma += num
   
print(f"Foram digitados {cont} e a soma deles sao {soma:.2f}")