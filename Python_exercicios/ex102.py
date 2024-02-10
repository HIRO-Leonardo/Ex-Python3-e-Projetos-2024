def fatorial(num=1, Show=False):
    """
    Função que faz fatoração

    Args:
        num (int, optional): numero que sera fatorado. Defaults to 1.
        Show (bool, optional): mostrara como foi feita a fatoração caso Show seja True
        Caso seja False so mostrara o resultado da fatoração . Defaults to False.
    """
    
    if Show == True:
        f = 1
        for c in range(num, 0, -1):
            f *= c
            if c != 1:
            
                print(f' {c} ', end='')
                
                print(' X ', end='')
            else:
                print(f' {c} ' , end='')
                
                    
        print(f'= {f}')
    if Show == False:
        f = 1
        for c in range(num, 0, -1):
            f *= c        
        print(f'{f}')
    
    
print(fatorial(1000, Show=True))
print(fatorial.__doc__)