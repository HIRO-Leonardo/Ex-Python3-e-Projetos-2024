cont = mai = men = 0
galera = []
dado = []
while True:
    dado.append(str(input("Nome: ")))
    dado.append(int(input("Peso: ")))
    continuar = str(input("Quer continuar[S/N]? ")).upper().split()[0]
    if len(galera) == 0 :
        mai = men = dado[1]
    else:
        if dado[1] > mai:
            mai = dado[1]
        if dado[1] < men:
            men = dado[1]
    cont += 1
    galera.append(dado[:])
    dado.clear()
    if continuar in 'N':
        break
print(f"Total de pessoas: {cont}")

print(f"Menor peso: {men}.. ", end=' ')
for p in galera:
    if p[1] == men:
        print(f"{p[0]} ",)
print(f"Maior peso: {mai}.. ", end='')
for p in galera:
    if p[1] == mai:
        print(f"{p[0]} ", end='' )  

