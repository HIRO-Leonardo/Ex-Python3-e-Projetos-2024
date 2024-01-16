cont_idade = cont_homen = cont_mulher = 0

while True:
    print("-"*10,"Cadastro de pessoas", "-"*10)
    idade = int(input("Digitge idade: "))
    print("-"*20)
    sexo = str(input("Digite o sexo [M/F]: ")).upper().split()[0]
    while sexo != 'M' and sexo != 'F':
        sexo = str(input("Digite o sexo [M/F]: ")).upper().split()[0]
    print("-"*20)
    resp = str(input("Quer continuar [S/N]: ")).upper().split()[0]
    while resp != 'N' and resp != 'S':
         resp = str(input("Quer continuar [S/N]: ")).upper().split()[0]
    print("-"*20)
    
    if idade > 18 and sexo in 'MF':
        cont_idade += 1
        
    if sexo in 'M':
        cont_homen += 1
        
    if sexo in 'F' and idade < 20:
        cont_mulher += 1
    if resp in 'N':
        break
        
print("-"*10,"RESULTADO DO CADASTRO DE PESSOAS","-"*10)  
print(f"total de pessoas com mais de 18 anos: {cont_idade}")
print("-"*20)
if cont_homen > 0:
    print("-"*20)
    print(f"Ao todo temos {cont_homen}, homens cadastrados ")
    print("-"*20)
else:
    print("-"*20)
    print("Nao foi cadastrado nenhum homem")
    print("-"*20)
if cont_mulher == 1 and cont_mulher == 0:
    print("-"*20)
    print("Nao foi cadastrado nenhuma mulher com menos de 20 anos")
    print("-"*20)
else:
    print("-"*20)
    print(f"E temos mulher {cont_mulher} com menos de 20 anos")
    print("-"*20)
    