def metade(preco=0, formato=False):
    res = preco / 2
    return res if formato is False else moeda(res)

def dobro(preco=0, formato=False):
    res = preco * 2
    return res if formato is False else moeda(res)

def menos13(preco=0, m=0, formato=False):
    m_total = m / 100 
    menos = preco * m_total
    res = preco - menos
    return res if formato is False else moeda(res)

def aumento10(preco=0, a=0, formato=False):
    a_total = a / 100 
    aum = preco * a_total
    res = preco + aum
    return res if formato is False else moeda(res)

def moeda(preco=0, moeda='R$'):
    
    return f'{moeda}{preco:>.2f}'.replace('.',',') 
     