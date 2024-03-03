try: 
    a = int(input('Numerador: '))
    b = int(input('Denominador: '))
    r = a / b
except (ValueError, TypeError):
    print('tivemos um problema com o tipo de dado inserido')
except ZeroDivisionError:
    print('Nao e possivel dividir numero por zero')
except KeyboardInterrupt:
    print('O usuario preferiu nao informar os dados')
except Exception as erro:
    print(f'O erro encontrado foi {erro.__class__}')
else:
    print(f'O resultado foi {r:.1f}')
finally:
    print('Muito obrigado!!! Volte sempre')