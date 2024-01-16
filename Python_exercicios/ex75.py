num = (int(input("Digite o primero numero: ")),
       int(input("Digite o segundo numero: ")),
       int(input("Digite o terceiro numero: ")),
       int(input("Digite o quarto numero: ")))
print(f"Voce digitou esses numeros {num} ")
print(f"Quantas vezes apareceu o 9: {num.count(9)} vezes")
if 3 in num:
    print(f"O 3 apareceu na posicao {num.index(3)+1}")
print("Os valores pares foraam digitados: ")
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
