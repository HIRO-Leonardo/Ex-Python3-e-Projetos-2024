from time import sleep

def contagem(inicio, fim, passo):
    if passo == 0:
        passo = 1
        if fim >= 1:
            fim1 = fim + 1
            
            print(f'Contagem do {inicio} ate o {fim} de {passo}: ')
            
            print('-'* 80)
            for c in range(inicio, fim1 , passo):
                print(f'{c} ==> ', end='', flush=True)
                sleep(0.1)
            print()
            print('-'* 80)
            
        if fim <= 0:
            passo = -1
            fim1 = fim - 1
            if passo <= 0:
                passo_negativo = abs(passo)
                fim_negativo = abs(fim)
                print(f'Contagem do {inicio} ate o {fim_negativo} de {passo_negativo}: ',)
                print('-'* 80)
                for c in range(inicio, fim1 , passo):  
                    print(f'{c} ==> ', end='', flush=True)
                    sleep(0.1)
                print()
                print('-'*70)
    else:
        
        if fim >= 1:
            fim1 = fim + 1
            print(f'Contagem do {inicio} ate o {fim} de {passo}: ')
            print('-'*70)
            for c in range(inicio, fim1 , passo):
                print(f'{c} ==> ', end='',flush=True)
                sleep(1.1)
            print()
            print('-'*70)
            
        if fim <= 0:
            fim1 = fim - 1
            if passo <= 0:
                passo_negativo = abs(passo)
                fim_negativo = abs(fim)
                print(f'Contagem do {inicio} ate o {fim_negativo} de {passo_negativo}: ',)
                print('-'*70)
                for c in range(inicio, fim1 , passo):  
                    print(f'{c} ==> ', end='', flush=True)
                    sleep(1.1)
                print()
                print('-'*70)
                
                
                                    
contagem(0, 10, 1)
contagem(10, 0, -2)
inicio = int(input("Digite o numero inicial: "))
fim = int(input("Digite o numero final: "))
passo = int(input("Digite o numero passo: "))
contagem(inicio, fim, passo)