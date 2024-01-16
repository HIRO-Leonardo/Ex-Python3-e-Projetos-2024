"""lista = [[],[],[]]
for c in range(0,3):
    valor = int(input(f"digite a matriz [0, {c}]: "))
    lista[0].append(valor)
for c1 in range(0,3):
    valor = int(input(f"Digite a matriz [1, {c1}]: "))
    lista[1].append(valor)
for c2 in range(0,3):
    valor = int(input(f"Digite a matriz [2, {c2}]: "))
    lista[2].append(valor)
print(f'{lista[0]}\n{lista[1]}\n{lista[2]}')
print()"""

matriz = [[0,0,0],[0,0,0],[0,0,0]]
for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite um numero da matriz [{l}, {c}]: "))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f" {matriz[l][c]:^5} ", end='')
    print()        
