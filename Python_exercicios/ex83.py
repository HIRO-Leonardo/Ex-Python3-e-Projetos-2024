expr = str(input("Digite uma espressao: "))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
            break
if len(pilha) == 0:
    print("Expressao esta valida:")
else:
    print("Expressao esta invalida")