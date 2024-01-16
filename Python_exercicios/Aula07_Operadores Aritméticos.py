"Ordem de precedencia "
"1: ()"
"2: **"
"3: * / // %"
"4: + -"


n1 = int(input("Digite um valor: "))
n2 = int(input("Digte outro valr: "))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2

print("A some é {}, o produto é {} e a divisao é {:.3f} ".format(s, m, d), end=' ')
print("Divisao inteira é {} e potencia é {}".format(di, e))
