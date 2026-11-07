Lista = [0]*10
media = 0
for i in range(10):
    Lista[i] = int(input(f'Digite o Vr da Lista Indice [{i}]: '))
    media += Lista[i]
media = media/10
print(f'UFC - Programação \nValores da Lista: {Lista} \nMedia = {media} \nFim do Trabalho')
