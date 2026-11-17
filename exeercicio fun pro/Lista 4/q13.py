n = int(input('digite o valor de n: '))
v = [0, 1]
a = 0
b = 1
c = a + b
print('UFC - Programação \nNome: Livia \nSequencia de Fibonacci:')
while c <= n:
    print(v)
    a = b
    b = c
    c = a + b
    v.append(c)
