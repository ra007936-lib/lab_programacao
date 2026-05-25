V=[]
D=[]
for x in range(10):
    n=int(input('Insira um valor: '))
    V.append(n)
for n in D:
    if n not in D:
        D.append(V)
print(f'Vetor: {V}')
print(f'Quantidade de valores diferentes {D}')