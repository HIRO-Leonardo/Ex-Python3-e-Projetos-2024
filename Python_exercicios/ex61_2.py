razao = int(input("Digite a razao: "))
pri_termo = int(input("Digite o termo: "))
termo = pri_termo
cont = 1
mais = 10
total = 0
while mais != 0:
    total = total + mais
    while cont <= total:
        print("{} --> ".format(termo), end='')
        cont += 1
        termo += razao
    print("Pausa")
    mais = int(input("Quantos termos a mais voce quer? "))
print("sessao finalizada com {} termos".format(termo))  
            
