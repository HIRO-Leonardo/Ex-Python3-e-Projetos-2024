def leiaint(msg):
    while True:
            try:
                n = int(input(msg))
                
            except (TypeError, ValueError):
                print('tivemos um problema com o tipo de dado inserido')
                continue
            except (KeyboardInterrupt)      :
               print('O usuario preferiu nao informar os dados')
               return 0 
            else:
                return n
    
    
def leiaFloat(msg):
    while True:
            try:
                n = float(input(msg))
                
            except (TypeError, ValueError):
                print('tivemos um problema com o tipo de dado inserido')
                continue
            except (KeyboardInterrupt)      :
               print('O usuario preferiu nao informar os dados')
               return 0.1 
            else:
                return n
            
            
numero_inteiro = leiaint('Digite o numero inteiro: ')
numero_real = leiaFloat('Digite o numero real: ')
print(f'Voçe acabou de digitar {numero_inteiro} e {numero_real}')
    