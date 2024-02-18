def leiaint(msg):
    ok = False
    valor = 0
    while True:
        numero_inteiro = str(input(msg))
        if numero_inteiro.isnumeric():
            valor = int(numero_inteiro)
            ok = True
        else:
            print('ERRO!!!! DIGITE UM NUMERO INTEIRO VALIDO')
        if ok:
            break
    return valor
    
numero_inteiro = leiaint('Digite o numero inteiro: ')
print(f'Voçe acabou de digitar {numero_inteiro}')
    
