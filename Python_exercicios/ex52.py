tot = 0
numero = int(input("Digite um numero: "))
for c in range(1, numero+1):

    if numero % c == 0:
        print("\033[33m", end='')
        tot += 1 
    else:
        print("\033[31m", end='')
    print("{}".format(c),end='')
print("\n\033[mO numero {} foi divisivel {} vezes".format(numero,tot))
if tot == 2:
    print("E por isso que ele e impar")
else:
    print("E poir isso que ele e par")