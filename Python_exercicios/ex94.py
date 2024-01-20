pessoa = dict()
resp = list()
soma = 0
media = 0   
cont = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input("Nome: "))
    while True:
        pessoa['Sexo'] = str(input("Sexo[M/F]: ")).upper().split()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print("ERRO, Digite somente M ou F")
    pessoa['idade'] = int(input("Idade: "))
    while True:
        continuar = str(input("Quer continuar[S/N]? ")).upper().split()[0]
        if continuar in 'SN':
            break
        print("ERRO, Digite somente S ou N")
    cont += 1
    soma += pessoa['idade']
    media = soma / cont
    resp.append(pessoa.copy())        
    if continuar in 'N':
        break   
print(resp)
print(pessoa)
print(f'Cadastro {cont}')
print(f'Media: {media:5.2f}')
print("Mulhres cadastradas ", end='')
for p in resp:
    if p['Sexo'] in 'F':
        print(f'{p["Nome"]} ', end='')
print()
for p in resp:
    if p['idade'] >= media:
        print(' ')
        for k, v in p.items():
            print(f'{k} = {v}', end='')
            print()
print("<<<<< ENCERRADO >>>>>")