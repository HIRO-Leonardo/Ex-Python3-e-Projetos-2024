nome = str(input("Digite seu nome completo: ")).strip()

divido = nome.split()

print(divido)
print("Seu nome completo: ".format(nome))
print("O primeiro nome informado e: {}".format(divido[0]))
print("O ultimo nome informado e: {} ".format(divido[-1]))
