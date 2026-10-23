n = int(input('digite o valor que deseja saber o fatorial: '))
cont = n
fat = 1
print('UFC - Programação \nNome: Ana Lívia')
while cont > 0:
    fat = fat * cont
    cont -= 1
print(f'Resultado do fatorial = {fat} \nValor de n = {n}')
