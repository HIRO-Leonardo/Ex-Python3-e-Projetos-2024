dias = float(input("Quantos dias foi usado o carro: "))
km_rodados = float(input("Quantos km foi rodado: "))
dia_usado = 60
km_rodado = 0.15
dia_total = dia_usado * dias
km_total = km_rodado * km_rodados
total_aluguel = dia_total + km_total

print("o carro foi usado por {:.2f} dias, rodou {:.2f}Km, entao o preco total do aluguel é R${:.2f}".format(dias, km_rodados, total_aluguel ))

