salario = float(input("Digite o valor do salario: R$"))
print("Valor do salario digiiado: R${:.2f}".format(salario))
if salario > 1250:
    reajuste = (salario * 0.109) + salario
    print("O novo valor do salario sera: R${:.2f}".format(reajuste))
if salario <= 1250:
    reajuste1 = (salario * 0.15) + salario
    print("O novo valor do salario sera: R${:.2f}".format(reajuste1))
    