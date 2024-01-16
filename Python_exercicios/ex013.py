salario = float(input("Digite o valor do salario: R$"))
reajuste = 15
total_atualizado = salario + (salario * reajuste/100)

print("O salario e R${}, o reajuste e de {}%, o salrio com reajuste e de R${}".format(salario ,reajuste, total_atualizado))