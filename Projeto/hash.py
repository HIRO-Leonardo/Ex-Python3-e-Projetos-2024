import hashlib

print("-"*10, "Bem vindo","-"*10)
opcao = int(input("""Digite quais das opcoes voce quer:
[1] Comparador de hash
[2] Criar hash
[3] brute force
: """))
if opcao == 1:
    hash1 = str(input("Digite o primeiro hash a ser comparada: "))
    hash2 = str(input("Digite a segunda hash a ser comparada: "))
    if hash1 == hash2:
        print(f"Primero hash digitado: {hash1}")
        print(f"segundo hash digitado: {hash2}")
        print("Sao iguais")
    else:
        print(f"Primero hash digitado: {hash1}")
        print(f"segundo hash digitado: {hash2}")
        print("Nao Sao iguais")
if opcao == 2:
     
    criar_hash = str(input("Digite o texto que quer criar a hash: ")).encode('utf-8')
    tipo_hash = str(input("""Digite qual tipo de hash vai escolher
[shaw512, md5, sha256 ,sha3_512, sha1, shake_256, blake2b, sha224]. 
Digite tudo em minusculo: """))
    
    if tipo_hash in 'shaw512':
        tipo_hash.encode('utf-8')
        m = hashlib.new('sha512')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'md5':
        tipo_hash.encode('utf-8')
        m = hashlib.new('md5')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'sha256':
        tipo_hash.encode('utf-8')
        m = hashlib.new('md5')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'sha3_512':
        tipo_hash.encode('utf-8')
        m = hashlib.new('sha3_512')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'sha1':
        tipo_hash.encode('utf-8')
        m = hashlib.new('sha1')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'blake2b':
        tipo_hash.encode('utf-8')
        m = hashlib.new('blake2b')
        m.update(criar_hash)
        print(m.hexdigest())
    elif tipo_hash in 'shake_256':
        tipo_hash.encode('utf-8')
        m = hashlib.new('shake_256')
        m.update(criar_hash)
        print(m.hexdigest())
    if tipo_hash in 'sha224':
        tipo_hash.encode('utf-8')
        m = hashlib.new('sha224')
        m.update(criar_hash)
        print(m.hexdigest())
if opcao == 3:
    print("Ainda esta em desenvolvimento")         
    