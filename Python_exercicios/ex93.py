futebol = {}
gols = []
time = list()
while True:
    futebol.clear()
    futebol['Nome'] = str(input("Nome do jogador: "))
    futebol['Quant partidas'] = int(input("Quantidades de partidas: "))
    gols.clear()
    for c in range(0,futebol['Quantidade de partidas']):
        gols.append(int(input(f"gols na partida {c}? ")))
        futebol['gols'] = gols[:]
    futebol['total'] = sum(gols)
    time.append(futebol.copy())
    while True:
        resp = str(input("Quer continuar? [S/N]")).upper().split()[0]
        if resp in 'SN':
            break
        print("ERRO, somente S ou N")
    if resp == 'N':
        break
print('cod', end='')
for i in futebol.keys():
    print(f"{i:<15}", end='')
print()
for k, v in enumerate(time):
    print(f'{k:>3}', end='')
    for d in v.values():
        print(f"{str(d):<15}", end='')
    print()
    
while True:
    busca = int(input("Mostar dados de qual jogador? (999 para parar): "))
    if busca == 999:
        break
    if busca >= len(time):
        print(f'ERRO, nao existe jogador com o codigo {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["Nome"]}:')
        for i, g in enumerate(time[busca] ['gols']):
            print(f'    No jogo {i} fez {g} gols')