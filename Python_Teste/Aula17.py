"""num = [1,2,3,4,5,6,7,8,9]
print("--"*20)
print(num)
print("--"*20)
num[3] = 11

num.append(12)
print("--"*20)
print(num)
print("--"*20)
print("--"*20)
num.sort()
print(num)
print("--"*20)
num.sort(reverse=True)
print(num)
print("--"*20)
print("--"*20)
num.insert(0,14)
print(num)
print("--"*20)
print("--"*20)
num.remove(2)
print(num)
print("--"*20)
print("--"*20)
if 15 in num:
    num.remove(15)
else:
    print("Numero nao foi encontrado")
    """
"""valores = []
for cont in range(0,5):
    valores.append(int(input("Digite o numero: ")))
#for v in valores:
    #print(f"{v}.. ", end='')
for c,v in enumerate(valores):
    print(f"Na posicao {c} encontrei o {v} ")"""
    
a = [1,2,3,4,5]
#Desse jeito o b nao vai copiar o a, e sim criar um ligacao entre as listas
b = a

#Para copiar uma lista usa exemplo: b = a[:]
b[2] =8
print(a)
print(b)