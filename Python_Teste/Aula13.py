"""for c in range(1001, 0, -1):
   print(c)
print("FIM")"""

"""n = int(input("Digite um numero: "))
for c in range(0, n+1):
    print('Oi')
print("FIM")"""

"""inicio = int(input("Inicio: "))
fim = int(input("Fim: "))
passo = int(input("Passo: "))
for c in range(inicio, fim+1, passo):
    print(c)
print("FIM")"""

s = 0
for c in range(0, 3):
    n = int(input("Digite um numero:")) 
    s += n
print("A somatoria dos numeros e {}".format(s))
