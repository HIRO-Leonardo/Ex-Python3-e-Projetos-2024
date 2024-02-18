def jogador(nome='<Desconhecido>', gols=0):
    
    print(f"O Jogador {nome} fez {gols} gol(s)")
    
        
    
nome = str(input("Nome do jogador: "))
gols = str(input("Gols: "))
if gols.isnumeric():
    gols = int(gols)
else:
    gols = 0
if nome.strip() == '':
    jogador(gols=gols)
else:
    jogador(nome,gols)
    
