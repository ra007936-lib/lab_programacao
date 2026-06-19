N=[]
for i in range(1, 6):
    n=float(input(f'Insira nota {i}° aluno:'))
    N.append(n)

menor = N[0]
for n in N:
    if n < menor:
        menor = n 
N.remove(menor)

print(N)