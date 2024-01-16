import random

aleatorio = random.randrange(5)


numero = int(input("Digite um numero de 0 a 5: "))

if numero == aleatorio:
    print("PARABENS, voce acertou")
else:
    print("OPS, voce errou tente novamente")