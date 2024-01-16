continuar = 'S'

while continuar in 'Ss':
    n1 = float(input("Digite a nota do AVA: "))
    n2 = float(input("Digite a nota da prova regular: "))
    
    media_Geral = (n1 * 0.40) + (n2 * 0.60)

    if media_Geral >= 5:
        print("Parabens, voce passou")
        print("Sua media e {:.2f}".format(media_Geral))
    else:
        print("Voces esta de exame, consulte no ava da data do exame")
        print("Sua media e de {:.2f}".format(media_Geral))
    continuar = str(input("Quer continuar? [S/N]: ")).upper().split()[0]

