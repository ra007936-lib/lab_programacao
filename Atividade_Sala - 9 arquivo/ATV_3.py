palavra=input('Digite um palavra: ').lower()
contador_vogais = 0
for letra in palavra:
    if letra in 'aeiou':
        contador_vogais += 1

print(f'A palavra {palavra} contém {contador_vogais} vogais')