a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))
c = int(input("Digite o terceiro numero: "))
print("-" *20)
print("Primeiro numero digitado {}\nSegundo digitado numero  {}\nTerceiro digitado numero {}".format(a,b,c))
print("-" *20)
# Verificando o menor numero
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
print("-" *20)   
print("Menor numero {}".format(menor))
print("-" *20)
# Verificando o maior numero
maior = b
if a>b and a>c:
    maior = b
if c>a and c>b:
    maior = c
print("-" *20)
print("O maior numero {}".format(maior))
print("-" *20)