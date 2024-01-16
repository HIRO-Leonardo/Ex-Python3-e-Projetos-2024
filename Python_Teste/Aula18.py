"""
teste = list()
teste.append('Leonardo')
teste.append(21)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 21
galera.append(teste[:])
print(galera)"""
galera = [['Maria', 21], ['Joao', 23], ['Daniel', 22], ['Leonardo', 21]]
print(galera[3][0])
"""for p in galera:
    print(f"Seu nome é {p[0]} e a idade {p[1]} ")
"""
galera = list()
dado = list()
totalmaior =  totalmenor  = 0
for c in range(0,3):
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Idade: ")))
    galera.append(dado[:])
    dado.clear()
print(galera)

for p in galera:
    if p[1] >= 21:
        print(f"{p[0]} e maior de idade")
        totalmaior += 1
    else:
        print(f"{p[0]} e menor de idade")
        totalmenor  += 1
print(f"No total {totalmaior} maiores e {totalmenor} menores")