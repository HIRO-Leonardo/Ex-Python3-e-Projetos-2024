sexo = str(input("Digite o sexo [M/F]: ")).upper().split()[0]

while sexo not in 'MmFf':
    sexo = str(input("Invalido, Dgitie novamente: ")).upper().split()[0]
    
print("foi cadastrado com sucesso: {}".format(sexo))