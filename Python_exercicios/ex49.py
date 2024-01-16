n = int(input("Digite um numero: "))
print("-"*20)
for c in range(0, 11, 1):
    print("-"*20)
    tabuada = n * c
    print("{} x {} = {}".format(n,c,tabuada))
    print("-"*20)
print("-"*20)