matriz = [[0,0,0],[0,0,0],[0,0,0]]
soma = mai = scol = 0

for l in range(0,3):
    for c in range(0,3):
        matriz[l][c] = int(input(f"Digite o numeroa matriz [{l}, {c}]: "))
print('-'*30)
for l in range(0,3):
    for c in range(0,3):
        print(f"{matriz[l][c]:^5}", end='')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
    print()
print(f"Soma {soma}") 
for l in range(0,3):
   scol += matriz[l][2]
print(f"Soma da terceira coluna {scol}")

if matriz[1][l] > mai:
    mai += matriz[1][l]
print(f"O maior valor da segunda linha {mai}")