n1 = int(input("Digite o primeiro valor: "))
n2 = int(input("Digite o segundo valor: "))
opcao = 0
while opcao != 5:
    print("""
    [1] Somar:                 
    [2] dividir
    [3] multiplicar
    [4] comparar       
    [5] Sair""")
    opcao = int(input("Digite um valor: "))
    if opcao == 1:
        resultado = n1 + n2
        print("A soma entre {} e {} e igual a {}".format(n1,n2,resultado))
    elif opcao == 2:
        resultado = n1 / n2
        print("O resultado da divisao entre {} e {} e de {}".format(n1,n2,resultado))
    elif opcao == 3:
        resultado = n1 * n2
        print("A multiplicacao entre {} e {} e de {}".format(n1,n2,resultado))
    elif opcao == 4:
        if n1 > n2:
            print("Comparacao entre {} e {} mostra que {} e maior que {}".format(n1,n2,n1,n2))
        elif n1 < n2:
             print("Comparacao entre {} e {} mostra que {} e menor que {}".format(n1,n2,n1,n2))
        elif n1 == n2:
             print("Comparacao entre {} e {} mostra que sao iguais".format(n1,n2))
        
print("Acabou")