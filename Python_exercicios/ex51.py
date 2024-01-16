termo = int(input("Digite o inicio do termo: " ))
razao = int(input("Digite a razao: "))
decimo = termo + (10 -1) * razao
for c in range(termo, 10, razao):
    print("{}".format(c), end=' ')
print("ACABOU")
    
