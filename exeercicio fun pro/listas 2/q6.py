m = int(input('digite o valor inicial da sequencia: '))
n = int(input('digite o vqlor final da sequencia: '))
par = 0
topar = 0
impar = 0
toimpar = 0
total = 0
print('UFC - Programação \nValores da Sequencia')
for i in range((n-m)+1):
    print(m, end=' ')
    if m%2==0:
        topar +=1
        par += m
    else:
        toimpar +=1
        impar += m
    total += m
    m+=1
print(f'\nvalor de m = {m - n} \nValor de N = {n} \nMedia os valores pares = {par/topar} \nMedia valores imapares = {impar/toimpar} \nSomatorio = {total} \nFim de Trabalho')
