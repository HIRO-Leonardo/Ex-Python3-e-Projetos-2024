lista = list() 
geral = list()
while True:
    nome = str(input("Nome: "))
    n1 = float(input("Nota 1: "))
    n2 = float(input("Nota 2: "))
    continuar = str(input("Quer continuar [S/N]? ")).upper().split()[0]
    media = (n1 + n2) / 2
    lista.append(nome)
    lista.append(n1)
    lista.append(n2)
    lista.append(media)
    geral.append(lista[:])
    lista.clear()
    if continuar in 'N':
        break
print("Dados")
for i,a in enumerate(geral):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
while True:
    detalhe = int(input("Digite o numero do aluno para ver as notas detalhadas (999 oara interonper): "))
    if detalhe <= len(geral):
        print(f"Notas de {geral[detalhe][0]} sao {geral[detalhe][1]}, {geral[detalhe][2]}")
    if detalhe == 999:
        break
