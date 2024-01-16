lista_geral = []
lista_par = []
lista_impar = []

while True:
    n = int(input("Digite um numero: "))
    continuar = str(input("Quer continuar [N/S]? ")).upper().split()[0]
    lista_geral.append(n)
    if n % 2 == 0:
        p = n
        lista_par.append(p)
    elif n % 2 == 1:
        i = n
        lista_impar.append(i)
    if continuar in 'N':
        break
    
lista_geral.sort()
lista_par.sort()
lista_impar.sort()
print(f"Lista geral {lista_geral}")
print(f"Lista so com numeros pares {lista_par}")
print(f"Lista so com numeros impares {lista_impar}")
    
    
