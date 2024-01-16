pri_termo = int(input("Digite o primeiro termo: "))
razao = int(input("Digite a razao: "))
termo = pri_termo
cont = 1
total = 0
mais = 10
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} -> ".format(termo), end='')
        termo += razao
        cont += 1
    print("Pausa")
    mais = int(input("quantos termos voce quer mostar a mais: "))
print("Sessao finalizada com {} termos mostrados".format(total))
