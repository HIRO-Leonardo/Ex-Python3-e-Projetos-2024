numero = float(input("Digite um numero para saber se e impar ou par: "))
resultado = numero % 2
print("numero informado: {:.2f}".format(numero))

if resultado == 0:
    print("O numero e par")
else:
    print("O numero e impar")