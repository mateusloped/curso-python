from random import randint
computador = randint(0,10)
print('''Sou seu computador, acabei de pensar  em um número de 0 a 10 . 
Será que você conseque acertar que número pensei?''')
acertou = False
palpite = 0
while not acertou:
    jogador = int(input('Digite o seu palpite: '))
    palpite += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS... tente mais uma vez: ')
        else:
            print('MENOS... Tente mais uma vez: ')
print('Parabéns, você acertou com {} tentativas'.format(palpite))
