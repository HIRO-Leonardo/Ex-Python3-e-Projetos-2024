expr = str(input("Digiie uma espressao: "))
pilha = []
for simb in expr:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
            break
if len(pilha) == 0:
    print("A expressao esta correta: ")
else:
    print("A expressao esta errada: ")