k = int(input('digite o valor de k: '))
l = int(input('digite o valor de l: '))
f = 0
for i in range(l):
    f += (k**(i+1))/(i+1)
print('UFC - Programação \nNome: Ana Lívia \nPrograma para calcular o valor de F')
print(f'Valor da função = {f} \nValor de K = {k} \nValor de L = {l}')
