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