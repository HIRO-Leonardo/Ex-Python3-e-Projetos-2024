def contagem(inicio, fim, passo):   
    for c in range(inicio, fim , passo):
        print('-'*5)
        print(c)
        print('-'*5)
        
        

contagem(0, 11, 1)
contagem(10, -1, -1)
inicio = int(input("Digite o numero inicial: "))
fim = int(input("Digite o numero final: "))
passo = int(input("Digite o numero passo: "))
contagem(inicio, fim, passo)