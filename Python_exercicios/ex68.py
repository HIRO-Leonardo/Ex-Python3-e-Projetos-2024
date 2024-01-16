import random
cont_ganhou = 0

par_impar = "P"
while True:
    print("-"*20)
    jogador = int(input("Digite um numero: "))
    print("-"*20)
    par_impar = str(input("Digite P para par e I para impar: ")).upper().split()[0]
    print("-"*20)
    computador = random.randint(0, 10)
    #print(computador)
    soma = jogador + computador
    resto = soma % 2
    print(soma)
    print(resto)
    if resto == 0 and par_impar in 'P':
        print("-"*20)
        print("Voce ganhou!!!!!")
        print("-"*20)
        cont_ganhou += 1
        print(f"Voce jogou o {jogador} e o computador jogou {computador}")
    elif resto == 0 and par_impar in 'I':
        print("-"*20)
        print("Voce perdeu!!!!")
        print("-"*20)
        print(f"Voce jogou o {jogador} e o computador jogou {computador}")
        break
    elif resto == 1 and par_impar in 'P':
        print("-"*20)
        print("Voce perdeu!!!!!")
        print("-"*20)
        print(f"Voce jogou o {jogador} e o computador jogou {computador}")
        break
    elif resto == 1 and par_impar in 'I':
        print("Voce ganhou!!!!!!")
        cont_ganhou += 1
        print(f"Voce jogou o {jogador} e o computador jogou {computador}")
if cont_ganhou == 1:
    print("-"*20)
    print(f"voce ganhou {cont_ganhou} vez")
    print("-"*20)
elif cont_ganhou == 0:
    print("-"*20)
    print(f"Voce nao ganhou nenhuma vez")
    print("-"*20)
else:
    print("-"*20)
    print(f"voce ganhou {cont_ganhou} vezes")
    print("-"*20)
    