nome = str(input("Digite seu nome:")).upper().strip()


print("o nome tem o total de {} letras ".format(len(nome)))
print("o nome tem o total de letras A: {} ".format(nome.count('A')))
print("O primeiro a aparece na posicao {}".format(nome.find('A')+1))
print("A ultima letra a aparece na posicao {}".format(nome.rfind('A')+1))
