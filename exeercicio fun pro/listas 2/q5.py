ap1 = float(input('insira a nota a primeira avaliação: '))
ap2 = float(input('insira a nota da segunda avaliação: '))
media = (ap1+ap2)/2
print('UFC - Programação \nPrograma para calcular a média e o resultado do Aluno \nCurso: Engenharia de computação \nNome: Ana Lívia')
print(f'primeira avaliação {ap1} \nSegunda avaliação {ap2}')
if media >= 7:
    print(f'Média = {media} \nResultado: Aprovado')
elif media >= 4 and media < 7:
    print(f'Média = {media} \nResultado: Prova Final')
else:
    print(f'Média = {media} \nResultado: Reprovado')
print('Fim de Trabalho')
