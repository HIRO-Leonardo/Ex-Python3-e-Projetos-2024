from time import sleep

def maior(* valores):
    maior = 0
    cont = 0
    print('\nAnalizando os numeros inseridos......')
    for valor in valores:
        print(f'{valor} ', end='', flush=True)
        sleep(0.3)
        if cont == 0 :
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print()
    print(f'Foram informados: {cont}')
    print(f'O maior numero informado: {maior}')

maior(5,6,0,9,2,1)