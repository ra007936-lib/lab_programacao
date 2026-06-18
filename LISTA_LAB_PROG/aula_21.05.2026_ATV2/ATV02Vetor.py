N1=int(input('Quantas notas de alunos: '))
N=[]
soma=0
for x in range(N1):
    N2=float(input('Insira notas {i+1°} alunos: '))
    N.append(N2)

for valor in N:
    soma += valor
media=soma / len(N)

proximo_da_media=N[0]
menor_distancia = abs(N[0]-media)
for valor in N:
    distancia_atual= abs(valor - media)
    if distancia_atual < menor_distancia:
        menor_distancia = distancia_atual
        proximo_da_media = valor
print(f'Vetor: {N}')
print(f'Média: {media:.1f}')
print(f'Valor mais próximo da média: {proximo_da_media}')