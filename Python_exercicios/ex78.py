"""valores = []
for cont in range(0,5):
    valores.append(int(input(f"Digite o numero na posicao {cont}: ")))
print(valores)
print(f"O menor valor e {min(valores)} e esta na posicao {valores.index(min(valores))}")
print(f"O maior valor e {max(valores)} e esta na posicao {valores.index(max(valores))}")"""

listanum = []
mai = 0 
men = 0
for c in range(0,5):
    listanum.append(int(input("Digite um valor: ")))
    if c == 0:
        mai = men =  listanum[c]
    else:
        if listanum[c] > mai:
            mai = listanum[c]
        if listanum[c] < men:
            men = listanum[c]
print(f"voce digitou {listanum}")
print(f"O maior valor foi {mai} na posicao", end='')
for i, v in enumerate(listanum):
    if v == mai:
        print(f"{i}... ",  end='')
print(f"O menor valor foi {men} na posicao", end='')
for i,v in enumerate(listanum):
    if v == men:
         print(f"{i}... ",  end='')
