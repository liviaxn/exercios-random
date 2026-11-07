n = int(input('Informe a quantidade de elementos da Lista: '))
lista = [0]*n
media = 0
quant = 0
for i in range(n):
    lista[i] = int(input(f'Digite o elemento {i} da lista: '))
    media += lista[i]
media = media/n 
for i in range(n):
    if lista[i] >= media:
        quant += 1
lista2 = [0]*quant
j = 0
for i in range(n):
    if lista[i] >= media:
        lista2[j] = lista[i]
        j += 1
print(f'UFC - Programação \nNome: Ana Lívia \nValores da Lista: {lista} \nValor da Média = {media} \nQuantiade maior/igual a media = {quant} \nElemnetos Maior/igual a media: {lista2} \nFim do Trabalho')
