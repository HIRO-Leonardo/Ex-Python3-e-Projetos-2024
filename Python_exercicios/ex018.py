import math
angulo = float(input("Digite um angulo:"))
seno = math.sin(math.radians(angulo))
cosseno = math.cos(math.radians(angulo))
tangente = math.tan(math.radians(angulo))


print("o abgulo de {}\ntem o seno de {:.2f}\n cosseno de {:.2f}\n tangente de {:.2f}".format(angulo, seno, cosseno, tangente))