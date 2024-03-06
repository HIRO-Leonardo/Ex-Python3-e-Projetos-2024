from time import sleep

def ajuda(msg):
    pesq = 'Pesquisando sobre o comando'
    print('-\033[1;33;45m' * len(pesq))
    print(pesq)
    print('-\033[1;33;45m' * len(pesq))
    print()
    sleep(1)
    sobre = 'Aqui esta reultado da pesquisa'
    print('-\033[1;33;45m' * len(sobre))
    print(sobre, f'{msg}')
    print('-\033[1;33;45m' * len(sobre))
    print()
    sleep(1)
    print('\033[1;33;44m')
    help(msg)
    print('\033[1;33;44m')
    print()
    sleep(1)
    fim = 'Pronto'
    print('- \033[1;33;44m' * len(fim))
    print(fim)
    print('- \033[1;33;44m' * len(fim))
    print()



while True:
    bemvindo = 'Bem vindo ao ajuda python3'
    print('- \033[1;33;44m' * len(bemvindo))
    print(bemvindo)  
    print('- \033[1;33;44m' * len(bemvindo))
    
    print()
    nome = str(input('Digite nome do comando que voce quer ajuda, Digite fim para encerrar o programa : ')).lower()
    print()
    if nome == 'fim':
        break
    if nome == '':
        break 
    sleep(1.1)
    ajuda(nome)
   
    