viagem = float(input("Digite a distancia da viagem em KM: "))

if viagem <= 200:
    custo_viagem = 0.5 * viagem
    print("O custo da viagem de {:.2F}Km é de R${:.2F}".format(viagem,custo_viagem))
else:
    custo_viagem_longa = 0.45 * viagem
    print("O custo da viagem de {:.2f}Km é de R${:.2f}".format(viagem,custo_viagem_longa))