pessoa = dict()
cont = cont_m = 0
while True:
    pessoa['Sexo'] = str(input("Sexo[M/F]: "))
    pessoa['idade'] = int(input("Idade: "))
    continuar = str(input("Quer continuar[S/N]? ")).upper().split()[0]
    if continuar not in 'SN':
            print("ERRO, Somente S ou N: ")
    if continuar in 'N':
        break