from  datetime import date

def votar(ano_nascimento):
    """
    pega o ano do nascimento e subtrai pelo ano atual ai tem a idade
    importamos a biblioteca do datetime especificamente date

    Args:
        ano_nascimento (_type_): Ano que a pessoa nasçeu

    Returns:
        i ele volta a idade da pessoa 
    """
    global i
    ano_atual = date.today().year
    
    i = ano_atual - ano_nascimento 
    return i


ano = int(input('Digite o ano que voce nasceu: '))
i = votar(ano)

print(votar.__doc__)

if i >= 16 and i < 18:
    print(f'Com {i} anos: VOTO OPCIONAL!!! ')
elif i >= 18 and i < 65:
    print(f'Com {i} anos: VOTO OBRIGATORIO!!! ')
elif i >= 65: 
    print(f'Com {i} anos: VOTO OPCIONAL!!! ')
elif i < 16 :
    print(f'Com {i} anos: NAO TEM IDADE SUFICIENTE PARA VOTAR, ESPERE FAZER 16 ANOS PARA VOTAR!!! ')