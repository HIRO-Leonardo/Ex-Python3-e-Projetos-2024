import operator
import random
from time import sleep
for c in range(1,5):
    dados = {'Jogador1':random.randint(1,10),
             'Jogador2':random.randint(1,10), 
             'Jogador3':random.randint(1,10),
             'Jogador4':random.randint(1,10)}
ranking = dict()
for k , v in dados.items():
    print(f'- {k} jogou {v}')
    sleep(2)
# transforma de dicionario em lista
ranking = sorted(dados.items(), key=operator.itemgetter(1), reverse=True)
for i ,v in enumerate(ranking):
    print(f'{i + 1} lugar {v[0]} com {v[1]}')
    sleep(1)