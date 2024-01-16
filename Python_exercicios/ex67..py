while True:
    n = int(input("Digite um numero: "))
    print("-"*30)
    if n < 0:
        break
    for c in range(0,11):
        vezes = n * c
        print(f"{n} x {c} = {vezes}")
    
print("acabou")