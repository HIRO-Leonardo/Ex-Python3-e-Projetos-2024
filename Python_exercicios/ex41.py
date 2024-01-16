from datetime import date

nome = str(input("Digite o nome: "))
ano_nascimento = int(input("Digite o ano que voce nasceu: "))
ano_atual = date.today().year

idade = ano_atual - ano_nascimento
print("Ola {}".format(nome))

if idade <= 9:
    print("Voce se encaixa na categoria Atleta mirim")
elif idade >= 10 and idade <= 14:
    print("Voce se encaixa na categoria Atleta Infantil")
elif idade >= 15 and idade <= 19:
    print("Voce se encaixa na categoria Atleta Junior")
elif idade >= 20 and idade <= 25:
    print("Voce se encaixa na categoria Atleta Senior")
elif idade >= 26:
    print("Voce se encaixa na categoria Atleta Master")