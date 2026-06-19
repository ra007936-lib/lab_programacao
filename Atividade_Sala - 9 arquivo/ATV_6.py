L=[]
for i in range(5):
    nm=input(f'Digite o nome {i+1}°: ')
    L.append(nm)
nomes_invertidos=[]
for i in range(1,6):
    nomes_invertidos.append(L[-i])

print(f'\nLista original: {L}')
print(f'\nLista invertida: {nomes_invertidos}')