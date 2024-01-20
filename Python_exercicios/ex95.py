
def terreno(largura,comprimento):
            terreno_total = largura * comprimento
            print("-"*20)
            print(f"Largura informado: {largura}")
            print(f"Comprimento informado: {comprimento}")
            print(f"Area total e de {terreno_total} metros quadrados")
            print("-"*20)

c = float(input("Comprimento: "))
l = float(input("Largura: "))
terreno(c,l)