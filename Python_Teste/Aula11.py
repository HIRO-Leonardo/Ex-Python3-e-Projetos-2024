nome = str(input("Digite seu nome: "))

if nome == 'Leonardo':
    print("Belo Nome")
elif nome == 'Carol' or 'Pedro' or 'Maria' or 'Joao':
    print("Nomes bem populares")
elif nome in 'Maria Carol Vera Tainara':
    print("Belo nome feminino")
else:
    print("nome normal")


print("Prazer em conhece-lo, {}".format(nome))