import math
co = float(input("Ente com o valor do cateto oposto: "))
ca = float(input("Entre com o valor do cateto adjacente: "))
hipotenusa = math.hypot(co, ca)

print("valor do cateto oposto:{}.\n valor do cateto adjacente: {}.\n o valor da hipotenusa e {}.".format(co,ca,hipotenusa))
