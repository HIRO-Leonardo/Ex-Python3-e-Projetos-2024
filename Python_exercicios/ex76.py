listagem = ('Lapis', 1.33,
            'Caneta', 1,
            'Intel-Core i7-13700k', 2600,
            'Z790 Rog Maximus', 3000,
            )
for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f"{listagem[pos]:.<30}", end=' ')
    else:
        print(f"R${listagem[pos]:>7.2f}")