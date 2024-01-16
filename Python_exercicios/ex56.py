maior_idade_homem = 0
soma_idade = 0
nome_velho = ''
total_mulher = 0 
for p in range(1,5):
    print("-"*20)
    nome = str(input("Digite o nome da {} pessoa: ".format(p))).strip()
    idade = float(input("Digite a idade: "))
    sexo  = str(input("Digite o sexo da pessoa [M/F]: ")).strip()
    print("-"*20)
    soma_idade += idade 
    if p == 1 and sexo == 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
            maior_idade_homem = idade
            nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        total_mulher += 1
media_idade = soma_idade/ 4 
print("A media das idades e de {}".format(media_idade))
print("O homem do mais velho e {} e tem {}anos ".format(nome_velho, maior_idade_homem)) 
print("Total de mulheres {}".format(total_mulher))   
