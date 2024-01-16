valor_produto = float(input("Digite o valor do produto: R$"))
metodo_pagamento = int(input("""Digite umas das formas de pagamento:
 [1] A Vista em dinheiro/cheque 10% DESCONTO
 [2] A Vista no cartao 5% DESCONTO
 [3] Em ate 2x no cartao
 [4] em 3x ou mais
 : """))

if metodo_pagamento == 1:
    print("Metodo de pagamento selecionado")
    desconto = valor_produto - (10/100 * valor_produto) 
    print("Voce ganhou 10% porcento de desconto")
    print("O valor do produto antes do desconto e de R${:.2f} e agora com desconto e R${:.2f}".format(valor_produto,desconto))
elif metodo_pagamento == 2:
    print("Metodo de pagamento selecionado")
    desconto = valor_produto - (5/100 * valor_produto)
    print("Voce ganhou 5% de desconto")
    print("O valor do produto antes do desconto e de R${:.2f} e agora com desconto e R${:.2f}".format(valor_produto,desconto))
elif metodo_pagamento == 3:
    print("Metodo de pagamento selecionado")
    print("O valor do produto R${:.2f}".format(valor_produto))
elif metodo_pagamento == 4:
    print("Metodo de pagamento selecionado")
    juros = valor_produto + (20/100 * valor_produto)
    print("Valor sem juros R${:.2f} e valor com juros pelo metodo de pagamento R${:.2f}".format(valor_produto, juros))