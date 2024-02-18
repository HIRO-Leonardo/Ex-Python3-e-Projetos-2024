def notas_escolares(* numeros, Show = False):
    """
    Pega a asa notas digitadas ve a quantidade, media, menor nota e maior nota.
    se caso o Show for True ele mostra a situacao a media da nota se é ruim, razoavel ou otima
    

    Args:
        Show (bool, optional):Mostra a situacao da media da nota se é ruim, razoavel ou otima. Defaults to False.
        *numeros: Recebe varios numeros
        
    Returns:
       return notas
       Onde notas é um dicionario
    """
    maior = 0
    cont = 0
    media = 0
    soma = 0
    notas = dict()
    for n in numeros:
        if n > maior:
            maior = n
        soma += n   
        cont += 1
        media = soma / cont
        
    notas['Total'] = cont
    notas['Maior nota'] = maior
    notas['Menor nota'] = min(numeros)
    notas['media'] = round(media, 2)
    if Show == True:
        if notas['media'] < 5:
            notas['Situação'] = 'RUIM'
        if  notas['media'] >= 5 and notas['media'] <= 7:
            notas['Situação'] = 'RAZOAVEL'
        if notas['media'] > 7:
            notas['Situação'] = 'OTIMA'
        
    return notas

notas = notas_escolares(3,15,10,10,10,1, Show=True)
print(notas) 
help(notas_escolares) 
    