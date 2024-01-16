"""for c in range(1,10):
        print(c)
print("FIM)
    """
c = 1
"""while c < 11:
    print(c)
    c += 1
print("ACABOU")"""
"""n = 1
while n != 0:
    n = int(input("DIGITE UM VALOR: "))
    
print("ACABOU")"""

"""r = 'S'
while r == 'S':
    n = int(input("DIGITE UM VALOR: "))
    r = str(input("QUER CONTINUAR [S/N]: ")).upper()
print("ACABOU")"""

n = 1
par = impar = 0 
while n != 0:
    n = int(input("DIGITE UM VALOR: "))
    if n != 0:
        if n % 2 == 0:
            par += 1
        else:
            impar +=1
print("{} NUMEROS PARES\n{} NUMEROS IMPARES".format(par,impar))
    