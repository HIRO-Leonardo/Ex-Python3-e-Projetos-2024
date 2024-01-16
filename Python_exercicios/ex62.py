n = int(input("Digite um numero: "))
t1 = 0
t2 = 1

if (n == 1) and (n == 2):
    print("1")
else:
    count = 3
    while count <= n:
        t3 = t1 + t2
        print(" {} ->".format(t3), end='')
        t1 = t2
        t2 = t3
        count += 1
print(" ACABOU")