lista1 =[1,2,3,4]
lista2 =[10,20,30,40,50,60]
lista_intercalada=[]
if len(lista1) <= len(lista2):
    menor, maior = lista1, lista2
else:
    menor, maior = lista2, lista1
for i in range(len(maior)):
    if (i < len(menor)):
        lista_intercalada.append(menor[i])
    lista_intercalada.append(maior[i])
print(f'lista1: {lista1}')
print(f'lista2: {lista2}')
print(f'lista_intercalada: {lista_intercalada}')