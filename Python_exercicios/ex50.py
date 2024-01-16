pares = 0
for c in range(1, 7):
    num = int(input("Digite um numero: "))
    if num % 2 == 0:
        pares = pares + num
        
print("A soma dos numeros e: {}".format(pares))