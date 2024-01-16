cont = 0
lista = []
while True:
    n = int(input("Digite um numero: "))
    continuar = str(input("Quer continuar? [S/N] : ")).upper().split()[0]
    lista.append(n)
    
    cont += 1
    if continuar in 'N':
        break
lista.sort(reverse=True)
print(lista)
print(f"Total de numeros digitados {cont}")
print(f"Em order descrecente {lista} ")
if 5 in lista:
    print(f"O valor 5 esta na lista na posicao {lista.index(5)}")
