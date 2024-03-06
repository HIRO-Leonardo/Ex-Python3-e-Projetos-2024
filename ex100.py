from random import randint
from time import sleep


def sorteio(lista):
    for cont in range(0,5):
        n = randint(0,100)
        lista.append(n)
        print(f'{n}  ', end='', flush=True)
        sleep(0.3)
        cont += 1
    print('PRONTO')
    
def somarPar(lista):
    soma = 0
    for valor in lista:
       if valor % 2 == 0:
            soma += valor
    print(f"Os valores {lista} somando os pares o total ifca em {soma}")
        


numero = list()
sorteio(numero)
somarPar(numero)

        
