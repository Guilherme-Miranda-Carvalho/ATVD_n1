import sys

print('Você está na sala 1')
print('Escolha seu caminho')
print('[1] caminho vermelho')
print('[2] caminho preto')

sala1=int(input())
while sala1== 1:
    print('Você esta na sala 2')
    print('Escolha seu caminho')
    print('[1] caminho vermelho')
    print('[2] caminho preto')
    sala2 = int(input())
    if sala2==1: # se a sala 2 eu escolher caminho 1 eu vou pra sala 3
        print(' voce esta na sala 3')
    elif sala2==2:
            print('Voce esta na sala 4') # se a sala 2 eu escolher caminho 2 eu vou pra sala 4
    
    while sala2 == 1: #aqui entra sala 3
        print('Escolha seu caminho')
        print('[1] caminho vermelho')
        print('[2] caminho preto')
        sala3 = int(input())

        if sala3 == 1:
            print('voce esta na sala 4')
        elif sala3 == 2:
            print('voce esta na sala 5')

    while sala2==2 :# aqui entra sala 4
        print('Escolha seu caminho')
        print('[1] caminho vermelho')
        print('[2] caminho preto')
        sala4 = int(input())
        if sala4==1:
              print('voce esta na sala 5')
        elif sala4==2:
              print(' você esta na sala 6 e so tem uma opção de escolha')
              print('voce esta na sala 8')
        break
    while sala3 == 1: #sala 4 fazer um return sala2
            print('Escolha seu caminho')
            print('[1] caminho vermelho')
            print('[2] caminho preto')
            sala4 = int(input())    
            if sala4==1:
                print('voce esta na sala 5')
            elif sala4==2:
                print(' você esta na sala 6 e so tem uma opção de escolha')
                print('voce esta na sala 8')
            break
    
    #while sala3==2:



    while sala4==1: #sala 5
           print('Escolha seu caminho')
           print('[1] caminho vermelho')
           print('[2] caminho preto')
           sala5=int(input())
           if sala5==1:
                 print('voce esta na sala 6 e so tem uma opção de escolha')
                 print('voce esta na sala 8')
           elif sala5==2:
                 print('voce esta na sala 7')
    while sala4==2: #sala 6
            print('Escolha seu caminho')
            print('[1] caminho vermelho')
            print('[2] caminho preto')
            sala8=int(input())
            if sala8==1:
                print('PARABENS, VOCÊ GANHOU O JOGO')
            elif sala8==2:
                 print('você entrou num portal e sera teletransportado')
                 print('escolha uma das opçoes abaixo')

    sys.exit()
while sala1 == 2:
    print('Você esta na sala 3')
    print('Escolha seu caminho')
    print('[1] caminho vermelho')
    print('[2] caminho preto')
    sala1 = int(input())
    if sala1== 1:
        print(' voce esta na sala 4')
    #elif caminho==2:
        #print('Voce esta na sala 4')
    else:
        print(' voce está na sala 5')
        break

print('Escolha seu caminho')
print('[1] caminho vermelho')
print('[2] caminho preto')
caminho1=int(input())
