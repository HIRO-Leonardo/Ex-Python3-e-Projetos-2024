co = float(input("Ente com o valor do cateto oposto: "))
ca = float(input("Entre com o valor do cateto adjacente: "))

hipotenusa = (ca ** 2 + co ** 2) ** (1/2)

print("valor do cateto oposto:{}.\n valor do cateto adjacente: {}.\n o valor da hipotenusa e {}.".format(co,ca,hipotenusa))
