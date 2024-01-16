dados = dict()
dados['Nome'] = str(input('Nome: '))
dados['Media'] = float(input('Media: '))
if dados['Media'] >= 5:
    dados['situacao'] = 'Aprovado'
else:
    dados['situacao'] = 'Reprovado'
print(f'Nome: {dados["Nome"]}')
print(f'Media: {dados["Media"]}')
print(f'Situação: {dados["situacao"]}')
for k , v in dados.items():
    print(f'- {k} e igual a {v}')