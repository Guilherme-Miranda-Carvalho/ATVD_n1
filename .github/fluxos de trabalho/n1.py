import random
print("Bem vindo ao dUAMgeun, um RPG onde sua guilda deve chegar até a sala 9 para vencer o jogo")
print("Você está na sala: 1\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")

#x = random.randint(1,5)
#print(f'{x}')

vermelho = 1
preto = 1
i = 1

while vermelho < 9:
    caminho = int(input(''))
    i = i + 1
    if caminho == 1:
        vermelho = vermelho + 1
        preto = vermelho
        print(f"Você está na sala: {vermelho}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    elif caminho == 2:
        preto = preto + 2
        vermelho = preto
        print(f"Você está na sala: {preto}\n Escolha seu caminho:\n [1] - Caminho vermelho\n [2] - Caminho Preto")
    else:
        print("Caminho inválido")
if i <= 7:
    print('\nParabens voce conseguiu comprir o desafio')
else:
    print(f'\nInfelizmente voce não compriu o desafio por usar {i} interações, \ntente novamente utilizando menos de 7 interações')
