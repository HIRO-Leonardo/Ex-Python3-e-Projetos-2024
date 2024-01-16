valor = float(input("Digite o valor do produto: R$"))
desconto = 5
valor_desconto = valor * 5/100
valor_final = valor - valor_desconto 
print("Valor do produto R${:.2f}, na promocao com desconto de {}% o valor vai fica em R${:.2f}".format(valor, desconto, valor_final))

