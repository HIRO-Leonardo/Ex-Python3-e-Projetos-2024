import random
jogador = int(input("Digite um numero entre 0 e 10: "))
computador = random.randint(0,10)
#print(computador)
acertou = False
palpites = 0
while not acertou:
    jogador = int(input("Errou, outro palpite: "))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print("Mais.... tente mais uma vez")
        elif jogador > computador:
            print("Menos.... tente mais uma vez ")
print("Acertou com {} tentativas . Parabens".format(palpites))
            