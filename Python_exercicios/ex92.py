from datetime import date

dados = dict()
dados['Nome'] = str(input("Nome: "))
ano_nascimento = int(input("Ano do nascimento: "))
ano = date.today().year
idade = ano - ano_nascimento
dados['idade'] = idade
dados['CTPS'] = int(input("Numero da carteira de trabalho, digite 0 se nao tiver: "))
dados['Sexo'] = str(input("Sexo[M/F]: ")).upper().split()[0]
if dados['CTPS'] == 0 :
    for i,k in dados.items():
        print(f"{i} tem o valor {k} ")
else:
    dados['Ano de contratacao'] = int(input("Ano da contratacao: "))
    dados['Salario'] = float(input("Salario: R$"))
    if dados['Sexo'] in 'F':
        aposentadoria = 30
        ano_contribuicao = dados['Ano de contratacao'] - ano
        ano_total = ano_contribuicao + idade + aposentadoria
        dados['Aposentadoria'] = ano_total
    if dados['Sexo'] in 'M':
        aposentadoria = 35
        ano_contribuicao = dados['Ano de contratacao'] - ano
        ano_total = ano_contribuicao + idade + aposentadoria
        dados['Aposentadoria'] = ano_total
    for i,k in dados.items():
        print(f"{i} tem o valor {k} ")
