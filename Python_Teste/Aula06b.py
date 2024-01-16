digite_algo = input("Digite alguma coisa: ")

print("tipo primitivo: ",type(digite_algo))
print("tem espaco? ",digite_algo.isspace())
print("e um numero? ",digite_algo.isascii())
print("e uma letra? ",digite_algo.isalpha())
print("e decimal?  ",digite_algo.isdecimal())