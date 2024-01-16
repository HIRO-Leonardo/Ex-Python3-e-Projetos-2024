numero = int(input("Digite um numero inteiro positivo: "))
unidade = numero // 1 % 10
dezena = numero // 10 % 10
centena = numero // 100 % 10
milhar = numero // 1000 % 10


print("Analizando o numero: {}".format(numero))
print("milhar {}\ncentena {}\ndezena {}\nunidade {}".format(milhar,centena,dezena,unidade))
 