"""def mensagem(msg):
    print('-'*30)
    print(   msg   )
    print('-'*30)
mensagem('Sitema Aluno')
mensagem('ERRO do sistema')
mensagem('Python')"""
"""
def soma(a,b):
    s= a + b
    print(s)


soma(3,5)
soma(2,9)
soma(2,8)
"""

# quando usa o sinal * e para desepacotamento:
"""
def soma(* valores):
    s = 0
    for num in valores:
        s += num
    print(f'Somando os {valores} temos {s}')
soma(5,4,3,3,3)
soma(0,4,3,2,1)

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1
valores = [3,4,6,5,2,3,1]
dobra(valores)
print(valores)
"""

#Aula 21 curso em video Python3

help(print)
print(input.__doc__)
print('-'*30)
from time import sleep
def contador(i,f,p):
    """
    faz contagem de um numero ate o outro
    
    Args:
         Param I: Inicio
         Param F: Fim
         Param P: Passos
    """
    c = i
    while c <= f:
        print(f'{c}', end='.. ', flush=True)
        sleep(0.3)
        c += p
    print('FIM!!')
contador(3,30,3)
print(contador.__doc__)

def somar(a=0,b=0,c=0):
    """
    Faz soma dos numeros

    Args:
        a (int, optional): . Defaults to 0.
        b (int, optional): . Defaults to 0.
        c (int, optional): . Defaults to 0.
        
    Se caso uns dos dos argumentos nao for informado ele valera o valor  0
    """
    soma = a + b +c
    print(f'A soma entres {a} + {b} + {c} = {soma}')
somar(5,4)
somar()
somar(b=4,c=5)
print(somar.__doc__)

print('-'*30)

def teste(b):
    global a
    a= 8
    b += 4
    c = 2
    print(f'Dentro da funcao teste A vale {a}')
    print(f'Dentro da funcao teste B vale {b}')
    print(f'Dentro da funcao teste C vale {c}')


a = 5
teste(a)
print(f'Fora da funcao teste A vale {a}') 

# Return

def somar1(a=0,b=0,c=0):
    s = a + b + c
    return s
r1 = somar1(1,5,3)
r2 = somar1(2,4)
r3 = somar1(4,0)
print(f'Os resultados sao: {r1}, {r2} e {r3}')

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

n =  int(input("Digite um numero: "))
print(f'O fatorial de {n} e igual a {fatorial(n)}')


def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um numero inteiro: '))
if par(num):
    print('E par')
else:
    print('E impar')    

a = (1,5,3) / 3 >= 6
print(a)