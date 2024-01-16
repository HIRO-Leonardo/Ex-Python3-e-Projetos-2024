peso = float(input("Digite seu peso: "))
altura = float(input("Digite sua altura: "))
imc = peso / (altura ** 2)
print("Seu IMC: {:.2f}".format(imc))
if imc < 18.5 and imc < 25:
    print("Seu IMC: Abaixo do peso")
elif imc >= 25 and imc < 30:
    print("Seu IMC: Peso Ideal") 
elif imc >= 30 and imc < 40:
    print("Seu IMC: Sobrepeso")
elif imc >= 40:
    print("Seu IMC: Obesidade Morbida")