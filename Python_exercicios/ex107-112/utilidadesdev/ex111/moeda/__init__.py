def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def menos13(preco=0, taxa=0, formato=False):
    m_total = taxa / 100 
    menos = preco * m_total
    res = preco - menos
    return res if formato is False else moeda(res)

def aumento10(preco=0, taxa=0, formato=False):
    a_total = taxa / 100 
    aum = preco * a_total
    res = preco + aum
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    
    return f'{moeda}{preco:>.2f}'.replace('.',',') 
     
def resumo(preco, taxa=0, taxar=0):
    print('-'*30)
    print('Resumo do valor'.center(30))
    print('-'*30)
    print(f'Preço analizado: {moeda(preco)}')
    print('-'*30)
    print(f'Dobro do preço: {dobro(preco, True)}')
    print('-'*30)
    print(f'Metade do preço: {metade(preco, True)}')
    print('-'*30)
    print(f'O aumento do Preço com {taxa}% : {aumento10(preco,taxa, True)} ')
    print('-'*30)
    print(f"Diminuindo do preco com {taxar}%: {menos13(preco, taxar, True)}")
    print('-'*30)
