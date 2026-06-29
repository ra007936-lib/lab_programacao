def celsius_para_fahrenheit(celsius):
    fahrenheit = (celsius * 1.8)+32
    return fahrenheit

print('--- CONVERSOR DE TEMPERATURA ---')
c = float(input('Digite a temperatura em C.: '))
print(f'A temperatura correspondente é: {celsius_para_fahrenheit(c)}')