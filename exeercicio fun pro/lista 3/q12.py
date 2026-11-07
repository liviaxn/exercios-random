n = int(input('digite o tamanho do conjunto: '))
lista = [0]*n
media = 0
quant = 0
for i in range(n):
    lista[i] = int(input(f'Digite o valor {i}: '))
    media += lista[i]
media = media/n 
for i in range(n):
    if lista[i] > media:
        quant += 1
print(f'UFC - Programação \nNome: Ana Lívia \nNúmero de elementos do conjunto = {n} \nElementos do conjunto: {lista} \nValor da Média = {media} \nQuantiade maior que a media = {quant}')
