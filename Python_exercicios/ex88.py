from random import randint
import time 
lista = list()
jogo = list()
total = 1
jogadas = int(input("Voce quer que eu sorteie quantas vezes? "))
while total <= jogadas:
    cont = 0
    while True:
        num = randint(1,60)
        if num not in lista:
            lista.append(num)
            cont += 1
        if cont >= 6:
            break
    total += 1
    lista.sort()
    jogo.append(lista[:])
    lista.clear()

print(f'Sorteando {jogadas} carreiras de numeros')    
for i, l in enumerate(jogo):
    print(f'jogo {i + 1}: {l}')     
    time.sleep(2)
print("ACABOU")
    