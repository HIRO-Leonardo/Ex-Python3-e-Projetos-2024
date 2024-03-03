from lib.sistema import *
from lib.arquivo import *
from time import sleep

arq = 'cursoemvideo.txt'

if not arquivoExiste(arq):
    criarArquivo(arq)


while True:
    resposta = menu(['Ver pessoas cadastradas', 'Cadastrar pessoa', 'Sair'])
    if resposta == 1:
        lerArquivo(arq)
    elif resposta == 2:
        nome = str(input("Nome: "))
        idade = leiaInt('Idade: ')
        cadastrar(arq,nome,idade)
    elif resposta == 3:
        print('Saindo do sistema')
        sleep(2)
        break
    else: 
        print('ERRO!!! DIGITE UMA OPCAO VALIDA')




