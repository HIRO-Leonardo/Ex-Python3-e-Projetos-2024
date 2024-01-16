cont = 0
soma = 0
num = 0
while num != 999:
    num = int(input("Digite um numero inteiro [para sair do programa digite 999]:"))
    cont += 1
    soma += num
print("Total de numeros digitados {} e a soma deles e de {}".format(cont - 1, soma - 999))