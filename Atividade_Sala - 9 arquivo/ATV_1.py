while True:
    num=int(input('Insira um número (0 - para sair): '))
    if num == 0:
        print('Encerando...')
        break
    if num >=10 and num <=50:
        print('Dado válido!')
    else:
        print('Dado inválido!')