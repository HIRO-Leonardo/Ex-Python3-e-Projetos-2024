cont = 0
menor_preco = 0
soma = 0
total_mil = 0
barato = ''
while True:
    nome_produto = str(input("Digite o nome do produto: "))
    valor_produto = float(input("Digite o valor do produto: "))
    continuar = str(input("Quer continuar [S/N]: ")).upper().split()[0]
    cont += 1
    soma += valor_produto
    if valor_produto > 1000:
        total_mil += 1
    if cont == 1 :
        menor_preco = valor_produto
        barato = nome_produto
    else:
        if valor_produto < menor_preco:
            menor_preco = valor_produto
            
    soma += valor_produto
    
    if continuar in 'N':
        break
print(f"Total de produtos comprados {cont}")
print(f"A soma de todos os itens e de R${soma:.2f}")
print(f"O menor valor foi de {menor_preco:.2f} e o nome do produto {barato}")
 