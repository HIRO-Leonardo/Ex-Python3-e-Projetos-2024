from datetime import date

sexo = int(input("Qual o seu sexo (1) para Masculino e (2) para Feminino: "))


if sexo == 1:
        nascimento = int(input("Digite ano que voce nasceu: "))
        anual = date.today().year
        idade = anual - nascimento
        if idade == 18:
            print("Voce tem que alistar IMEDIATAMENTE")
        elif idade < 18:
            saldo = 18 - idade
            print("Ainda falta  {} anos para se alistar ".format(saldo))
            ano = anual + saldo
            print("Seu alistmento sera em {}".format(ano))
        elif idade  > 18:
            saldo = idade - 18
            print("Voce ja deveria ter se alistado ha {} anos".format(saldo))
            ano = anual - saldo
            print("Seu alistamento foi em {}".format(ano))
elif sexo== 2:
    print("Sexo Feminino nao presica de alistar")
else:
    print("Numero invalido")


