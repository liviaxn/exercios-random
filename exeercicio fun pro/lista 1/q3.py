print('UFC - Programação \nCálculo de Raízes de uma equação de Segundo Grau')
a = float(input('Digite o valor de a: '))
b = float(input('Digite o valor de b: '))
c = float(input('Digite o valor de c: '))
delta = (b*b) - (4*a*c)
if delta < 0:
    print('Não tem raízes reais')
else:
    x1 = ((b*-1)+(delta**0.5))/2*a
    x2 = ((b*-1)-delta)/2*a
    if x1 == x2:
        print(f'Valor de Delta = {delta} \nValor de X1 = {x1}')
    else:
        print(f'Valor de Delta = {delta} \nValor de X1 = {x1}, \nValor de X2 = {x2}')

