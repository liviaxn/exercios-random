print('Programa para gerar uma sequência de M a N')
m = int(input('Digite o valor inicial da sequência M: '))
n = int(input('Digite o valor final da sequência N: '))
p =0
print(f'UFC - Programação \nPrograma para gerar uma Sequência de {m} a {n}')
for i in range(n - m + 1):
    print(m, end=' ')
    if m%2==0:
        p += m
    m+=1
print(f'\nValor de M = {m - n} \nValor de N = {n} \nSomatório dos valores pares = {p}')

