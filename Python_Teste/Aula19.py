"""pessoas = {'Nome': 'Leonardo', 'Sexo': 'M', 'Idade': 21 }
print(f'O {pessoas["Nome"]} tem {pessoas["Idade"]} idade')
print(pessoas.keys())
print(pessoas.items())
print(pessoas.values())
for k in pessoas.keys():
    print(k,)
for k, i in pessoas.items():
    print(f'{k} = {i}')
"""
"""
brasil = list()
estado1 = {'uf': 'Rio de Janeiro', 'Sigla': 'RJ'}
estado2 = {'uf': 'Sao Paulo', 'Sigla': 'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(brasil[1]['Sigla'])
"""
brasil = list()
estado = dict()
for c in range(0,3):
    estado['uf'] = str(input("Unidade federativa: "))
    estado['sigla'] = str(input("Sigla: "))
    brasil.append(estado.copy())
for e in brasil:
    for v in e.values():
        print(f"{v} ", end=' ')
    print()
