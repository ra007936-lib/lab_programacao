num=int(input('Digite um número inteiro positivo: '))
produto = 1
for i in range(1, num + 1, 2):
    produto *= i

print(f'O produto dos impares até `{num} é: {produto}')