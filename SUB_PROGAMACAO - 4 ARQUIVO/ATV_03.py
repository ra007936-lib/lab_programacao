def permitir_acesso(idade):
    idade = 2026 - idade
    if idade >= 2008:
        return('True')
    else:
        return('False')

print('--- VALIDADOR DE SISTEMA ---')
i=int(input('Digite seu ano de nacimento: '))
if permitir_acesso(i) in 'True':
    print(f'Boas vinda você tem {i} anos')
else:
    print(f'Bloqueio! menor de idade você tem {i} anos')