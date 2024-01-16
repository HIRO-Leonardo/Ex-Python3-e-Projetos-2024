velocidade =  float(input("Digite a quantos km/h foi registrado: "))

if velocidade > 80:
    print("Velocidade: {}KM/H".format(velocidade))
    print("Voce esta acima da velocidade permitida, foi multado")
    conta = velocidade - 80
    multa_valor =  7 * conta
    print("Valor da multa R${:.2f}".format(multa_valor))
elif velocidade == 80:  
    print("VOce esta no limite de velocidade")

else:
    print("TUDO OK!!")    
    