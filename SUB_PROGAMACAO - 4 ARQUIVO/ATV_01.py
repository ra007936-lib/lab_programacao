def calculador_notas(media):
    if nt >= 6:
        return('Aprovado')
    elif nt >= 4:
        return('Verificação Sumplentar')
    else:
        return('Reprovado')

nt=float(input('Insira a média do aluno: '))
print(f'Status do aluno: {calculador_notas(nt)}')



