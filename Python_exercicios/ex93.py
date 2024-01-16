futebol = {}
gols = []
futebol['Nome'] = str(input("Nome do jogador: "))
futebol['Quantidade de partidas'] = int(input("Quantidades de partidas: "))
for c in range(0,futebol['Quantidade de partidas']):
    gols.append(int(input(f"gols na partida {c}? ")))
    futebol['gols'] = gols[:]
futebol['total'] = sum(gols)
print("-"*30)
print(futebol)
print("-"*30)

for k, v in futebol.items():
    print(f"O {k} tem o valor {v}")
    
print("-"*30)
print(f' O jogador {futebol["Nome"]} jogou {futebol["Quantidade de partidas"]} partidas')
for i,v in enumerate(futebol["gols"]):
    print(f' => partida {i} fez {v} gols  ')