import random

print("BEM VINDO AO GAME PEDRA, PAPEL E TESOURA: ")

jogada = int(input("Digite [0]PEDRA, [1]PAPEL e [2]TESOURA: "))
itens = ('Pedra', 'Papel', 'Tesoura')
computador = random.randint(0,2)
print(computador)
if computador == 0: # Joga pedra
    if jogada == 0:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Empate")
    if jogada == 1:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Ganhou")
    if jogada == 2:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Perdeu")
    
elif computador == 1:
    if jogada == 0:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Perdeu") 
    if jogada == 1:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Empate")
    if jogada == 2:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Ganhou")
elif computador == 2:
     if jogada == 0:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Ganhei") 
     if jogada == 1:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Perdeu")
     if jogada == 2:
        print("o computador jogou: {}".format(computador))
        print("O jogador jogou: {}".format((jogada)))
        print("Empate")
    
