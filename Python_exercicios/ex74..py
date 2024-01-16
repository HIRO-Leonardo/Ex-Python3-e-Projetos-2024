import random

sorteio = (random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10),random.randint(0,10))
print("Foram sorteados esses numeros: ")
for n in sorteio:
    print(f"{n} ", end='')
    
print(f"\nO maior valor e {max(sorteio)}")
print(f"O menor valor e {min(sorteio)}")