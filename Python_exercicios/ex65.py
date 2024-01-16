cont = 0
divisao = 0
soma = 0 
maior = menor = 0
continuar = 'S'
while continuar in 'Ss':
    numero =  int(input("Digite um numero inteiro: "))
    cont +=1
    soma += numero
    continuar = str(input("Quer continuar [S/N]: ")).upper().split()[0]
    if cont == 1:
        maior = menor = numero
    else:
        if numero > maior:
            maior = numero
        if numero < menor:
            menor = numero
            
divisao = soma / cont
print("A soma dos numeros {}, media {}, quantos numeros foram digitados {}".format(soma,divisao,cont))
print("O maior numero {} e o menor numero {} ".format(maior, menor))
    