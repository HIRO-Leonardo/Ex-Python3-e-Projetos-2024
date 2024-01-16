r1 = float(input("Digite o primeiro valor: "))
r2 = float(input("Digite o segundo valor: "))
r3 = float(input("Digite o terceiro valor: "))

if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    if r1 == r2 == r3:
        print("Os valores informados consegue formar um triangulo EQUILATERO")
    if r1 == r2 != r3:
        print("Os valores informados consegue formar um triangulo ISOSCELES")
    if r1 != r2 != r3 != r1:
        print("Os valores informados consegue formar um triangulo ESCALENO")
else:
    print("Os valores informados nao consegue formar um triangulo")