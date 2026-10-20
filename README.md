print('Progarma para gerar uma sequência')
m = int(input('\nDigite o valor inicial da sequencia de M: '))
n = int(input('\ndigite o valor final da sequencia N: '))
print('UFC - Programação \nPrograma para gerar sequencia \nSequencia:')

for i in range((n-m)+1):
    print(m, end=" ")
    m+=1
print(f'\nValor de M = {m-n} \nValor de N = {n} \nFim de Trabalho')
