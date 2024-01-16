numero_extenso = ('zero', 'um','dois','tres','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','quatorze','quinze','dezesseis','dezesete','dezoito','dezenove','vinte')

while True:
    num = int(input("Digite o numero de 1 ate 20: "))
    if 0 <= num <= 20:
        break
    print("Digitou errado")
print(f"O numero selecionado {num} por extenso e {numero_extenso[num]}") 
    



