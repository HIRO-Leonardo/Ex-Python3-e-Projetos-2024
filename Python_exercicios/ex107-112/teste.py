from utilidadesdev.ex111 import moeda
import utilidadesdev.dado 

#p = float(input("Digite um valor em R$"))

"""
print(f'Dobro de {ex109.moeda(p)} é {ex109.dobro(p, True)}')
print(f'Metade de {ex109.moeda(p)} é {ex109.metade(p, True)}')
print(f'Diminundo 13% de {ex109.moeda(p)} é {ex109.menos13(p, 13)}')
print(f'Aumentando 10% de {ex109.moeda(p)} é {ex109.aumento10(p, 10)}')
"""
n = utilidadesdev.dado.leiadinheiro('Digite o preço: R$')
p1 = moeda.resumo(n, 10, 13)
