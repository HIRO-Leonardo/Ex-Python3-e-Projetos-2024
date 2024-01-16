nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2
print("Primeira nota {} + Segunda nota {} Media {}".format(nota1, nota2, media))
if media >= 7:
    print("Parabens voce foi APROVADO")
elif media >= 5.0 and media <= 6.9:
    print("Esta de RECUPERACAO, Estude mais")
elif media <= 4.9:
    print("Voce foi REPROVADO")