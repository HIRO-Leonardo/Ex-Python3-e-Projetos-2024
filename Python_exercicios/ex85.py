lista = [[],[]]
valor = 0
for c in range(1,8):
    valor = int(input(f"Digite {c} numero: "))
    if valor % 2 == 0:
        lista[0].append(valor)
    else:
        lista[1].append(valor)
print(f"Lista {lista}")
lista[0].sort()
lista[1].sort()
print(f"Pares: {lista[0]}")
print(f"Impares: {lista[1]}")


