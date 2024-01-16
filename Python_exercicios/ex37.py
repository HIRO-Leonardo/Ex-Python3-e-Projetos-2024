numero = int(input("Digite um numero inteiro: "))
opcao = int(input("""
[1] BINARIO
[2] OCTAL
[3] HEXADECIMAL                  
Digite uma opcao de 1 a 3: """))

if opcao == 1:
    print("{} convertido em BINARIO e {}".format(numero, bin(numero)[2:]))
elif opcao == 2:
    print("{} Convertido em OCTAL e {}".format(numero, oct(numero)[2:]))
elif opcao == 3:
    print("{} Convertido em HEXADECIMAL e {}".format(numero, hex(numero)[2:]))