quantos_anos = float(input("Quantos anos e o emprestimo: "))
valor_financiamento = float(input("Valor do financiamento: R$"))
salario = float(input("Digite o salario: R$"))
ano = 12
total_anos =  ano * quantos_anos
parcelas = valor_financiamento / total_anos
porcentagem = (30/100) * salario
print("Valor do imovel a ser financiado R${:.2f}".format(valor_financiamento))
print("Salario do comprador R${:.2f}".format(salario))
print("Qauntos meses da duracao das pacelas: {:.0f} Meses".format(total_anos))
print("Valor das parcelas R${:.2f}".format(parcelas))
print("-------Alizando-Pedido-------" )
if parcelas >= porcentagem:
    print("No momento nao podemos oferecer o empretimo")
    print("Tente novamente daqui a 6 meses")
else:
    print("Parabens voce conseguiu o emprestimo")


