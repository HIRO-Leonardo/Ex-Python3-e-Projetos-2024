#import modulo
from uteis import numeros



num = int(input("Digite um valor: "))
fat = numeros.fatorial(num)
print(f'O fatorial de {num} é {fat}')
dobro = numeros.dobro(num)
print(f'O dobro de {num} é {dobro}')